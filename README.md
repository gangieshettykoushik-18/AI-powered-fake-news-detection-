# AI-powered-fake-news-detection-
A machine learning system that detects whether a news headline or article is likely to be fake or real.
# 📰 Fake News Detection using AI & NLP

## 📌 Overview
This project is an AI-powered Fake News Detection system using **Natural Language Processing (NLP)** and **Machine Learning**.  
It can predict whether a given news headline or article is **fake** or **real**.

## 🚀 Features
- Data cleaning & preprocessing
- TF-IDF text vectorization
- Logistic Regression classification
- Interactive web app using Streamlit
- Model persistence using Joblib

🏃 Run Locally
Train the model:

python src/train.py

Run the web app:
streamlit run app/app.py

📈 Example Output

FAKE News → 🚨 This news seems FAKE

REAL News → ✅ This news seems REAL

🔮 Future Improvements

Use BERT or DistilBERT for better accuracy

Deploy as a public web app

Multi-language news detection
