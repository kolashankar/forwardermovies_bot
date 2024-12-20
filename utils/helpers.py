import re
from telegram.constants import ParseMode

def clean_text(text):
    # Remove excess whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    return text

def format_message(text, format_type='markdown'):
    if format_type == 'markdown':
        # Escape special characters
        text = re.sub(r'([_*\[\]()~`>#+\-=|{}.!])', r'\\\1', text)
    elif format_type == 'html':
        # Replace special characters with HTML entities
        text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return text

def get_parse_mode(format_type):
    if format_type == 'markdown':
        return ParseMode.MARKDOWN_V2
    elif format_type == 'html':
        return ParseMode.HTML
    else:
        return None

