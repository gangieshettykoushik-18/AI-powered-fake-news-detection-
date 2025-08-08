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

fake-news-detection/
│
├── data/
│   ├── raw/                  # Original dataset
│   └── processed/            # Cleaned dataset
│
├── notebooks/                # Jupyter notebooks for EDA and modeling
│   ├── 01_data_cleaning.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_model_training.ipynb
│
├── src/                      # Source code
│   ├── preprocess.py         # Text preprocessing functions
│   ├── train.py              # Model training script
│   ├── predict.py            # Prediction script
│
├── app/                      # Streamlit/Flask app
│   ├── app.py
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
