from langdetect import detect, LangDetectException

class LanguageFilter:
    @staticmethod
    def filter_by_language(message, allowed_languages):
        if not message.text:
            return True
        
        try:
            detected_language = detect(message.text)
            return detected_language in allowed_languages
        except LangDetectException:
            return True  # Allow messages where language can't be detected

    @staticmethod
    def get_language(text):
        try:
            return detect(text)
        except LangDetectException:
            return None

