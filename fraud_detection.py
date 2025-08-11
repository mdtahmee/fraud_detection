import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("fraud_detection_pipeline. pkl")  # Fixed extra space in file name

# App settings
st.set_page_config(page_title="Fraud Detection App", page_icon="💳", layout="wide")
# Custom CSS
st.markdown("""
    <style>
        /* Black background */
        .stApp {
            background-color: #000000;
            color: white;
        }

        /* Centered title */
        h1 {
            color: #00e6e6;
            text-align: center;
            font-weight: bold;
        }

        /* Prediction result card */
        .result-card {
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
        }

        /* Fraud styling */
        .fraud {
            background-color: #330000;
            border: 2px solid #ff4d4d;
            color: #ff4d4d;
        }

        /* Safe styling */
        .safe {
            background-color: #003300;
            border: 2px solid #33cc33;
            color: #33ff33;
        }

        /* Sidebar styling */
        .css-1d391kg {
            background-color: #1a1a1a;
            padding: 10px;
            border-radius: 10px;
        }
    </style>
"""

, unsafe_allow_html=True)

# Main title
st.title("💳 Fraud Detection Prediction App")
st.markdown("<p style='text-align:center;'>Enter transaction details in the sidebar and click <b>Predict</b>.</p>", unsafe_allow_html=True)

# Sidebar for inputs
st.sidebar.header("📝 Transaction Details")
transaction_type = st.sidebar.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.sidebar.number_input("💰 Amount", min_value=0.0, value=1000.0, step=100.0)
oldbalanceOrg = st.sidebar.number_input("🏦 Old Balance (Sender)", min_value=0.0, value=10000.0, step=500.0)
newbalanceOrig = st.sidebar.number_input("🏦 New Balance (Sender)", min_value=0.0, value=9000.0, step=500.0)
oldbalanceDest = st.sidebar.number_input("📥 Old Balance (Receiver)", min_value=0.0, value=0.0, step=500.0)
newbalanceDest = st.sidebar.number_input("📥 New Balance (Receiver)", min_value=0.0, value=0.0, step=500.0)

# Prediction
if st.sidebar.button("🔍 Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]  # Probability of fraud

    # Result card
    if prediction == 1:
        st.markdown(f"<div class='result-card fraud'>🚨 This transaction <b>MAY BE FRAUD</b><br>Probability: {probability:.2%}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='result-card safe'>✅ This transaction <b>LOOKS SAFE</b><br>Probability of fraud: {probability:.2%}</div>", unsafe_allow_html=True)



