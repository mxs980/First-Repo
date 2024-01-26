from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer

class Vectorizer:
    """Convert text to vector form using TF-IDF vectorization."""
    
    def __init__(self):
        # You could potentially save and load vectorizers to ensure consistency
        # across different sessions
        self.vectorizer = TfidfVectorizer()

    def fit_texts(self, texts: List[str]):
        """Fit TF-IDF to texts to ready the transformation."""
        self.vectorizer.fit(texts)

    def transform_text(self, text: str) -> List[float]:
        """Transform a single text string into a vector."""
        return self.vectorizer.transform([text]).toarray().tolist()[0]
