import sublime_plugin
import re

def to_camel_case(text):
    text = re.sub("_(\w)", lambda _: _.group(1).upper(), text)
    text = text[0].upper() + text[1:]
    return text

def to_snake_case(text):
    return re.sub('(?<=[^_])([A-Z])', r'_\1', text).lower()

class CamelSwitchCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command('expand_selection', {'to': 'word'})

        for region in self.view.sel():
            word = self.view.substr(region)
            if re.match('[a-z]*_[a-z]*', word) or re.match('[a-z]+', word):
                replace = to_camel_case(word)
            else:
                replace = to_snake_case(word)
            self.view.replace(edit, region, replace)
