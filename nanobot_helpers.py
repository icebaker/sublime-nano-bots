import sublime

from .nanobot import NanoBot
from .sublime_helpers import SublimeHelpers


class NanoBotHelpers:
    @staticmethod
    def config():
        settings_keys = ['NANO_BOTS_API_ADDRESS', 'NANO_BOTS_STREAM']

        def load_settings(source, keys):
            if isinstance(source, dict):
                return {
                    key: source.get(key) for key in keys if key in source}
            if hasattr(source, "has"):
                return {
                    key: source.get(key) for key in keys if source.has(key)}
            return {}

        default_settings = sublime.load_settings('Default.sublime-settings')
        user_settings = sublime.load_settings('Preferences.sublime-settings')
        project_data = sublime.active_window().project_data() or {}
        project_settings = project_data.get('settings', {})
        view_settings = SublimeHelpers.view().settings()

        config = {key: default_settings.get(key) for key in settings_keys}

        for settings in [user_settings, project_settings, view_settings]:
            config.update(load_settings(settings, settings_keys))

        return config

    @staticmethod
    def stop():
        NanoBot.stop()

    @staticmethod
    def cartridges_as_menu():
        cartridges = NanoBotHelpers.cartridges()

        items = []

        for cartridge in cartridges:
            if cartridge['meta']['symbol']:
                items.append(
                    (cartridge['meta']['symbol'] + ' ' +
                     cartridge['meta']['name'], cartridge))
            else:
                items.append(cartridge['meta']['name'])

        return items

    @staticmethod
    def cartridges():
        return NanoBot.cartridges(NanoBotHelpers.config())

    @staticmethod
    def cartridge(cartridge_id):
        return NanoBot.cartridge(NanoBotHelpers.config(), cartridge_id)

    @staticmethod
    def evaluate(cartridge, state, input, mode, prefix):
        params = {
            'cartridge': cartridge, 'state': state,
            'input': input, 'mode': mode, 'prefix': prefix}

        config = NanoBotHelpers.config()

        NanoBot.perform(
            config, params,
            lambda result:
                NanoBotHelpers.on_output(
                    {'config': config, 'params': params},
                    result))

    @staticmethod
    def on_output(environment, result):
        if environment['config']['NANO_BOTS_STREAM']:
            content = result['fragment']
        else:
            content = result['output']

        selection = SublimeHelpers.selection()

        if selection['region'] is not None:
            SublimeHelpers.insert_text(
                '',
                selection['region'],
                environment['params']['mode'],
                environment['params']['prefix'])

        SublimeHelpers.insert_text(
            content, None,
            environment['params']['mode'], environment['params']['prefix'])
