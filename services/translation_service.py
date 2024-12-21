from translate import Translator

class TranslationService:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text, target_language):
        try:
            translation = self.translator.translate(text, dest=target_language)
            return translation.text
        except Exception as e:
            print(f"Translation error: {str(e)}")
            return text  # Return original text if translation fails

    def detect_language(self, text):
        try:
            detection = self.translator.detect(text)
            return detection.lang
        except Exception as e:
            print(f"Language detection error: {str(e)}")
            return None

    def get_supported_languages(self):
        return self.translator.LANGUAGES

    def translate_message(self, message, target_language):
        if message.text:
            message.text = self.translate(message.text, target_language)
        if message.caption:
            message.caption = self.translate(message.caption, target_language)
        return message

