from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

# Load pre-trained model
model = pickle.load(open('model/sentiment_model.pkl', 'rb'))
vectorizer = pickle.load(open('model/vectorizer.pkl', 'rb'))

# Basic text cleaning
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        review = request.form['review']
        clean_review = clean_text(review)
        review_vector = vectorizer.transform([clean_review])
        prediction = model.predict(review_vector)[0]
        return render_template('result.html', review=review, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
