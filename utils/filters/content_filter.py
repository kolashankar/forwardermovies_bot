from telegram.ext import MessageFilter
from config.constants import Constants

class ContentFilter(MessageFilter):
    def __init__(self, allowed_types=None):
        self.allowed_types = allowed_types or Constants.ALLOWED_CONTENT_TYPES

    def filter(self, message):
        if message.text and 'text' in self.allowed_types:
            return True
        if message.photo and 'photo' in self.allowed_types:
            return True
        if message.video and 'video' in self.allowed_types:
            return True
        if message.document and 'document' in self.allowed_types:
            return True
        if message.audio and 'audio' in self.allowed_types:
            return True
        return False

    def set_allowed_types(self, allowed_types):
        self.allowed_types = allowed_types

