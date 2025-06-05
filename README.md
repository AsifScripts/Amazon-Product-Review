🛒 Amazon Product Review Sentiment Analysis (Flask + ML + Bootstrap)
A simple web application that analyzes Amazon product reviews using Machine Learning (ML) and Natural Language Processing (NLP) to predict whether the review is Positive, Negative, or Neutral.

Built with Python, Flask, scikit-learn, and Bootstrap 5, this project is user-friendly, lightweight, and deployable on Render.

live :- https://amazon-product-review-1.onrender.com

📊 Project Overview
Input a product review.

The app processes the review using NLP techniques.

A Machine Learning model predicts the sentiment.

Results are displayed on a clean, modern web interface.

🛠️ Tech Stack
Layer	Technology Used
Programming	Python 3.x
ML/NLP	scikit-learn, TfidfVectorizer
Web Framework	Flask
Frontend	Bootstrap 5, HTML, CSS
Deployment	Render (https://render.com)

📁 Project Structure
csharp
Copy
Edit
amazon-review-analysis/
│
├── app.py                # Flask Application
├── train_model.py        # ML Model Training Script
├── model/                # Saved Model & Vectorizer (.pkl files)
├── templates/            # HTML (Bootstrap UI)
│   ├── index.html
│   └── result.html
├── static/               # CSS and Static Files
│   └── css/
│       └── styles.css
├── requirements.txt      # Project Dependencies
├── .gitignore            # Ignored Files/Folders
└── README.md             # Project Documentation

🚀 Local Setup Instructions
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/AsifScripts/Amazon-Product-Review.git
cd amazon-review-analysis

2️⃣ Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

4️⃣ Train the Sentiment Model (Optional)
bash
Copy
Edit
python train_model.py
This will create the model and vectorizer files inside the model/ directory.

5️⃣ Run the Flask App
bash
Copy
Edit
python app.py
Open your browser and visit:
➡️ http://127.0.0.1:5000/

🌐 Deploying on Render
What is Render?
Render.com is a modern cloud platform to deploy web apps easily, similar to Heroku but with a free plan.

Deployment Steps:
Push your project to GitHub.

Sign up on Render.

Click on "New Web Service".

Connect your GitHub repo.

Configure:

Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app

Choose Free Tier (or paid if needed).

Deploy 🚀

Render Link:
🔗 [https://render.com](https://amazon-product-review-1.onrender.com)

![Screenshot 2025-05-16 115250](https://github.com/user-attachments/assets/ba8bf256-1fcb-40b4-b2f4-576e1df50bb0)

![Screenshot 2025-05-16 115244](https://github.com/user-attachments/assets/93deeaf0-f319-458c-829b-78d6b977ce1f)


✅ Features Summary
Real-time review sentiment analysis.

Clean, responsive Bootstrap UI.

Lightweight and fast.

Easily extendable to advanced models (BERT, LSTM, etc.).

Deployable on free cloud (Render).

📝 License
MIT License - Free to use, modify & distribute.

🙌 Credits
Built by asifScripts

Inspired by Amazon product review datasets and common NLP use cases.
