import time

import sublime

from .sublime_helpers import SublimeHelpers


class NanoBotState:
    _instance = None
    state = {'status': 'waiting', 'thread': None}
    _status_updater = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def stop(self):
        if self.state['thread'] is not None:
            self.state['thread'].set()
            self.state['thread'] = None
        self.state['status'] = 'stopped'

    def update(self, cartridge, new_state=None):
        if new_state is not None:
            self.state = new_state

        if self.state['status'] != 'pending':
            if self._status_updater is not None:
                sublime.set_timeout_async(
                    lambda: sublime.cancel_timeout(self._status_updater), 0)

            SublimeHelpers.view().set_status('nano-bots', '')
            return

        text = ''

        if cartridge['meta']['symbol'] is None:
            text += '🤖'
        else:
            text += cartridge['meta']['symbol']

        text += ' ' + cartridge['meta']['name'] + '... '

        seconds = time.time() - self.state['started_at']

        text += '(' + str(int(seconds)) + 's)'

        SublimeHelpers.view().set_status('nano-bots', text)

        self._status_updater = sublime.set_timeout(
            lambda: self.update(cartridge), 1000)
