import re

class FilterService:
    @staticmethod
    def should_forward(task, message):
        if not message.text:
            return True

        # Check blacklist
        if task.filter_keywords:
            blacklist = task.filter_keywords.split(',')
            for word in blacklist:
                if word.strip().lower() in message.text.lower():
                    return False

        return True

    @staticmethod
    def apply_replacements(task, text):
        if not task.replace_keywords:
            return text

        replacements = dict(item.split(':') for item in task.replace_keywords.split(','))
        for old, new in replacements.items():
            text = re.sub(r'\b' + re.escape(old.strip()) + r'\b', new.strip(), text, flags=re.IGNORECASE)

        return text

    @staticmethod
    def set_remove_keywords(user, keywords):
        user.filter_keywords = ','.join(keywords)

    @staticmethod
    def set_replace_keywords(user, replacements):
        user.replace_keywords = ','.join([f"{k}:{v}" for k, v in replacements.items()])

    @staticmethod
    def clear_replace_keywords(user):
        user.replace_keywords = None

    @staticmethod
    def add_to_blacklist(user, words):
        current_blacklist = user.filter_keywords.split(',') if user.filter_keywords else []
        current_blacklist.extend(words)
        user.filter_keywords = ','.join(set(current_blacklist))

    @staticmethod
    def remove_from_blacklist(user, words):
        if not user.filter_keywords:
            return

        current_blacklist = user.filter_keywords.split(',')
        updated_blacklist = [word for word in current_blacklist if word not in words]
        user.filter_keywords = ','.join(updated_blacklist) if updated_blacklist else None

