import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from config.bot_config import bot_config
import numpy as np

class MachineLearningService:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.classifier = MultinomialNB()
        self.model_path = 'ml_model.joblib'
        self.load_model()

    def train_model(self, texts, labels):
        X = self.vectorizer.fit_transform(texts)
        X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)
        self.classifier.fit(X_train, y_train)
        accuracy = self.classifier.score(X_test, y_test)
        logging_service.info(f"Model trained with accuracy: {accuracy}")
        self.save_model()

    def predict(self, text):
        X = self.vectorizer.transform([text])
        return self.classifier.predict(X)[0]

    def save_model(self):
        joblib.dump((self.vectorizer, self.classifier), self.model_path)
        logging_service.info("Model saved successfully")

    def load_model(self):
        try:
            self.vectorizer, self.classifier = joblib.load(self.model_path)
            logging_service.info("Model loaded successfully")
        except FileNotFoundError:
            logging_service.warning("No existing model found. A new model will be trained.")

    async def update_model(self, texts, labels):
        self.train_model(texts, labels)

    async def classify_content(self, text):
        prediction = self.predict(text)
        confidence = np.max(self.classifier.predict_proba(self.vectorizer.transform([text])))
        return prediction, confidence

