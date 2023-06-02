import sublime
import sublime_plugin

from .sublime_helpers import SublimeHelpers
from .nanobot_helpers import NanoBotHelpers


class NanoBotsCommand(sublime_plugin.TextCommand):
    def run(
        self, edit,
        action, mode='replace', prefix='', format='[prompt]: [input]',
        state='-', cartridge=None, input=None
    ):
        environment = {'command': self, 'edit': edit}
        params = {
            'action': action, 'mode': mode, 'prefix': prefix, 'format': format,
            'state': state, 'cartridge': cartridge, 'input': input}

        NanoBotsDispatcher.run(environment, params, 0)


class NanoBotsDispatcher:
    @staticmethod
    def run(environment, params, counter):
        if counter > 2:
            sublime.error_message(
                'Too many input requests: {}'.format(counter))
            return

        if params['action'] == 'stop':
            NanoBotHelpers.stop()
            return

        if params['cartridge'] is None:
            NanoBotsDispatcher.ask_for_cartridge(environment, params, counter)
            return

        if params['action'] == 'evaluate':
            selection = SublimeHelpers.selection()
            if selection['text'] == '':
                return

            NanoBotHelpers.evaluate(
                params['cartridge'], params['state'],
                selection['text'], params['mode'], params['prefix'])

        if params['action'] == 'prompt':
            if params['input'] is None or params['input'] == '':
                NanoBotsDispatcher.ask_for_input(environment, params, counter)
                return

            NanoBotHelpers.evaluate(
                params['cartridge'], params['state'],
                params['input'], params['mode'], params['prefix'])

        if params['action'] == 'apply':
            selection = SublimeHelpers.selection()
            if selection['text'] == '':
                return

            if params['input'] is None or params['input'] == '':
                NanoBotsDispatcher.ask_for_input(environment, params, counter)
                return

            text_input = params['format'].replace(
                '[prompt]', params['input']
            ).replace('[input]', selection['text'])

            NanoBotHelpers.evaluate(
                params['cartridge'], params['state'],
                text_input, params['mode'], params['prefix'])

    @staticmethod
    def ask_for_cartridge(environment, params, counter):
        def on_done(options, index):
            if index == -1:
                return
            params['cartridge'] = options[index][1]['system']['id']

            NanoBotsDispatcher.run(environment, params, counter + 1)

        def open(options):
            environment['command'].view.window().show_quick_panel(
                list(map(lambda option: option[0], options)),
                lambda index:
                on_done(options, index)
            )

        NanoBotHelpers.cartridges_as_menu(open)

    @staticmethod
    def ask_for_input(environment, params, counter):
        def on_done(input):
            params['input'] = input

            NanoBotsDispatcher.run(environment, params, counter + 1)

        environment['command'].view.window().show_input_panel(
            'Prompt', '', on_done, None, None
        )
