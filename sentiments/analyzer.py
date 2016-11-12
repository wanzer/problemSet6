import nltk
from nltk.tokenize import TweetTokenizer
class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives="positive-words.txt", negatives="negative-words.txt"):
        """Initialize Analyzer."""

        # TODO
        self.positives = positives
        self.negatives = negatives
        self.sentiment_score = 0

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        # TODO
        self.sentiment_score = 0
        token = TweetTokenizer()
        text_list = token.tokenize(text)
        for text in text_list:
            for word in open(self.positives).readlines():
                if text == word.rstrip():
                    self.sentiment_score += 1
            for word in open(self.negatives).readlines():
                if text == word.rstrip():
                    self.sentiment_score -= 1
        return self.sentiment_score
        
