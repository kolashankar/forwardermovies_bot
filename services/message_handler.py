from .filter_service import FilterService
from .text_service import TextService
from .translation_service import TranslationService
from .watermark_service import WatermarkService

class MessageHandler:
    def __init__(self):
        self.filter_service = FilterService()
        self.text_service = TextService()
        self.translation_service = TranslationService()
        self.watermark_service = WatermarkService()

    def process_text(self, user, text):
        if not self.filter_service.should_forward(user, text):
            return None

        text = self.filter_service.apply_replacements(user, text)
        text = self.text_service.add_begin_end_text(user, text)
        
        if user.translation_enabled:
            text = self.translation_service.translate(text, user.target_language)

        return text

    def process_photo(self, user, photo):
        if not self.filter_service.should_forward(user, photo):
            return None

        caption = photo.caption or ""
        caption = self.filter_service.apply_replacements(user, caption)
        caption = self.text_service.add_begin_end_text(user, caption)

        if user.translation_enabled and caption:
            caption = self.translation_service.translate(caption, user.target_language)

        if user.watermark_enabled:
            photo = self.watermark_service.add_watermark(photo, user.watermark_text)

        return photo, caption

    def process_document(self, user, document):
        if not self.filter_service.should_forward(user, document):
            return None

        caption = document.caption or ""
        caption = self.filter_service.apply_replacements(user, caption)
        caption = self.text_service.add_begin_end_text(user, caption)

        if user.translation_enabled and caption:
            caption = self.translation_service.translate(caption, user.target_language)

        return document, caption

