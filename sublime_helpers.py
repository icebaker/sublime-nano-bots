import sublime
import sublime_plugin


class InsertTextCommand(sublime_plugin.TextCommand):
    def run(self, edit, mode, text, prefix, region=None):
        if mode == 'replace' and region is not None:
            self.view.replace(edit, sublime.Region(*region), text)
        else:
            for position in self.view.sel():
                if region is not None:
                    text = prefix + text

                    self.view.sel().clear()
                    self.view.sel().add(
                        sublime.Region(position.end(), position.end()))

                self.view.insert(edit, position.end(), text)


class SublimeHelpers:
    @staticmethod
    def view():
        return sublime.active_window().active_view()

    @staticmethod
    def insert_text(content, region, mode, prefix):
        sublime.set_timeout(
            lambda: SublimeHelpers.view().run_command(
              'insert_text',
              {'text': content, 'region': region,
               'mode': mode, 'prefix': prefix}),
            0
        )

    @staticmethod
    def selection():
        view = SublimeHelpers.view()
        selected_region = None
        selected_text = ''
        for region in view.sel():
            if not region.empty():
                selected_region = (region.begin(), region.end())
                selected_text += view.substr(region)
                break

        return {'region': selected_region, 'text': selected_text}

    @staticmethod
    def clear_selection():
        def _clear_selection():
            view = SublimeHelpers.view()
            for region in view.sel():
                start = region.begin()
                view.sel().clear()
                view.sel().add(sublime.Region(start, start))

        sublime.set_timeout(_clear_selection, 0)
