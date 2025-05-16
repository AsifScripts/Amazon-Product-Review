import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Example data
texts = [
    "I love this product, it's amazing",
    "Worst purchase ever, completely useless",
    "Very satisfied with the quality",
    "Not good, I expected better",
    "Average product, okayish performance"
]
labels = ['Positive', 'Negative', 'Positive', 'Negative', 'Neutral']

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

# Save model and vectorizer
pickle.dump(model, open('model/sentiment_model.pkl', 'wb'))
pickle.dump(vectorizer, open('model/vectorizer.pkl', 'wb'))
