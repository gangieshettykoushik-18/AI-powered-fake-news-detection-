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

## 📂 Project Structure
fake-news-detection/
│
├── data/
│ └── raw/ # Original dataset
│
├── model/ # Saved ML model & vectorizer
│
├── src/
│ ├── preprocess.py # Text cleaning
│ ├── train.py # Train and save model
│
├── app/
│ └── app.py # Streamlit app
│
├── requirements.txt
└── README.md