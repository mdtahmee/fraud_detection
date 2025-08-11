# 💳 Fraud Detection Prediction App

An **AI-powered Streamlit web application** that predicts whether a financial transaction is **fraudulent** or **legitimate** using a trained machine learning pipeline.  
It features an **interactive interface** and a **sleek dark-themed design**.

---

## 🚀 Live Demo

Check out the live application here:  
**[Fraud Detection App on Streamlit](https://frauddetection2025.streamlit.app/)**

---

## ✨ Key Features

- ⚡ **Real-time Predictions** – Instantly check if a transaction may be fraud.
- 📊 **Probability Insights** – See risk percentages for each transaction.
- 🎨 **Dark Mode UI** – Red alerts for fraud, green for safe transactions.
- 🌐 **Easy Deployment** – Works on Streamlit Cloud and other hosting platforms.

---

## 📸 Screenshots

### 🏠 Home Page
<img width="1917" height="857" alt="Home Page" src="https://github.com/user-attachments/assets/aa7f4ca6-b4c3-4f96-ac05-dbd476916e35" />

### 🚨 Fraud Prediction Example
<img width="1897" height="857" alt="Fraud Prediction" src="https://github.com/user-attachments/assets/f949f3ed-efcc-4c52-8773-3c739c41b429" />

### ✅ Safe Transaction Example
<img width="1903" height="855" alt="Safe Transaction" src="https://github.com/user-attachments/assets/8835508d-86bc-4c07-b2ef-b87ddb1f512f" />

---

## 📂 Project Structure

fraud_detection/
│
├── fraud_detection.py # Streamlit app source code
├── fraud_detection_pipeline.pkl # Trained ML model
├── requirements.txt # Python dependencies
├── screenshots/ # App screenshots (optional local copies)
└── README.md # Project documentation



---

## 🛠 Technology Stack

- **Python 3.11**
- **Streamlit** – Interactive web app framework
- **Pandas, NumPy** – Data processing
- **Scikit-learn** – Machine learning
- **Joblib** – Model serialization
- **Matplotlib, Plotly, Seaborn** – Data visualization

---

## ⚙ How It Works

1. **User Input** – Transaction type, amount, and account balances.
2. **ML Model** – Pre-trained pipeline processes input and predicts fraud likelihood.
3. **Output** – Shows:
   - 🚨 **Fraud Alert** – High risk
   - ✅ **Safe Transaction** – Low risk

---

## 🖥 Setup & Deployment

### Run Locally

git clone https://github.com/<your-username>/fraud_detection.git
cd fraud_detection
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
streamlit run fraud_detection.py

Deploy on Streamlit Cloud
Push your project to GitHub.

Go to Streamlit Cloud.

Click New app → Connect your GitHub repo.

Select:

Branch: main

Main file path: fraud_detection.py

Click Deploy – Your app will be live in seconds.



Author
MD Tahmeed
📧 Email: mdtahmeed2003@gmail.com
🌐 GitHub | LinkedIn

yaml
Copy
Edit

