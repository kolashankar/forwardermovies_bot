import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

nltk.download('punkt')
nltk.download('stopwords')

class ContentCategoryFilter:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
        self.classifier = MultinomialNB()
        self.categories = []

    def train(self, texts, labels):
        self.categories = list(set(labels))
        X = self.vectorizer.fit_transform(texts)
        self.classifier.fit(X, labels)

    def predict_category(self, text):
        X = self.vectorizer.transform([text])
        return self.classifier.predict(X)[0]

    def filter_by_category(self, message, allowed_categories):
        if not message.text:
            return True
        
        predicted_category = self.predict_category(message.text)
        return predicted_category in allowed_categories

    def save_model(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump((self.vectorizer, self.classifier, self.categories), f)

    def load_model(self, filename):
        with open(filename, 'rb') as f:
            self.vectorizer, self.classifier, self.categories = pickle.load(f)

