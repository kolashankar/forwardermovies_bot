import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

class AutoTagger:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def extract_tags(self, text, num_tags=5):
        words = word_tokenize(text.lower())
        words = [word for word in words if word.isalnum() and word not in self.stop_words]
        
        word_freq = Counter(words)
        return [word for word, _ in word_freq.most_common(num_tags)]

    def tag_message(self, message, num_tags=5):
        if message.text:
            tags = self.extract_tags(message.text, num_tags)
        elif message.caption:
            tags = self.extract_tags(message.caption, num_tags)
        else:
            tags = []
        
        return tags

    def suggest_hashtags(self, text, num_tags=5):
        tags = self.extract_tags(text, num_tags)
        return ['#' + tag for tag in tags]

