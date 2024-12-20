import re

class RegexFilter:
    @staticmethod
    def filter_by_regex(message, pattern):
        if not message.text:
            return True
        
        return bool(re.search(pattern, message.text))

    @staticmethod
    def replace_by_regex(text, pattern, replacement):
        return re.sub(pattern, replacement, text)

