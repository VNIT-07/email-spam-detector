import streamlit as st
import joblib

# Load your trained model + vectorizer

model = joblib.load('email_dt_model.pkl')
vectorizer = joblib.load('email_tfidf_vectorizer.pkl')

st.title("📧 Email Category Predictor (Spam / Ham)")

# Input box for email text
email_text = st.text_area("Enter your email text:")

# When the user clicks the button
if st.button("Predict"):
    if email_text.strip() == "":
        st.warning("Please enter some text to predict.")
    else:
        # Vectorize the input
        email_vec = vectorizer.transform([email_text])
        
        # Predict
        prediction = model.predict(email_vec)[0]
        
        # Show result
        st.success(f"The email is predicted as: **{prediction.upper()}**")
