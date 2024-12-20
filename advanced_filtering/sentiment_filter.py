from textblob import TextBlob

class SentimentFilter:
    @staticmethod
    def filter_by_sentiment(message, min_polarity=0):
        if not message.text:
            return True
        
        analysis = TextBlob(message.text)
        return analysis.sentiment.polarity >= min_polarity

    @staticmethod
    def get_sentiment(text):
        analysis = TextBlob(text)
        return analysis.sentiment.polarity

