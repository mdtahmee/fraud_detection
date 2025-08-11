
# ​ Fraud Detection Prediction App

An **AI-powered Streamlit web application** that predicts whether a financial transaction is **fraudulent** or **legitimate** using a trained machine learning pipeline. It features an interactive interface and sleek dark-themed design.

---

##  Live Demo

Check out the live application here:
**[Live Demo on Streamlit](https://frauddetection2025.streamlit.app/)**

---

##  Key Features

- **Real-time Predictions**: Enter transaction details and instantly receive a fraud score.
- **Probability Insights**: Visual indicators showing how risky a transaction appears.
- **Stylish Dark Theme**: Dark UI with red alerts for fraud and green for safe transactions.
- **Easy Deployment**: Optimized for Render and other popular hosting platforms.

---

##  Project Structure


---

##  Technology Stack

- **Python 3.11**
- **Streamlit** – UI framework  
- **Pandas & NumPy** – Data handling  
- **Scikit-learn** – Trained ML model  
- **Joblib** – Model serialization  
- **Matplotlib, Plotly, Seaborn** – Visualizations

---

##  How It Works

1. **User Input**: Transaction type, amount, and account balances.
2. **Model Pipeline**: Encodes input and predicts fraud status.
3. **Result Output**:
   -  **🚨 Fraud Alert**, with risk percentage  
   -  **✅ Safe Transaction**, with confidence score  

---

## ​ Setup & Deployment

### Run Locally
```bash
git clone https://github.com/<your-username>/fraud_detection.git
cd fraud_detection
python -m venv venv
source venv/bin/activate         # Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
streamlit run fraud_detection.py


Deployment
Deploy on Streamlit Cloud
Push your project to GitHub.

Go to Streamlit Cloud.

Click "New app" → Connect your GitHub repo.

Select:

Branch: main

Main file path: fraud_detection.py

Click Deploy – Your app will be live in seconds!

💡 Example: Live Fraud Detection App



✨ Author
MD Tahmeed
📧 Email: mdtahmeed2003@gmail.com
🌐 GitHub | LinkedIn
