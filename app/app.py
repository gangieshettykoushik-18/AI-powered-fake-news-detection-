STREAMLIT APP

import streamlit as st
import joblib
from preprocess import clean_text

# Load model and vectorizer
model = joblib.load("model/fake_news_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

st.title("📰 Fake News Detection App")
st.write("Enter a news article or headline to check if it's Fake or Real.")

user_input = st.text_area("News Text:")

if st.button("Check"):
    if user_input.strip() != "":
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]
        if prediction == 1:
            st.error("🚨 This news seems **FAKE**")
        else:
            st.success("✅ This news seems **REAL**")
    else:
        st.warning("Please enter some text.")

