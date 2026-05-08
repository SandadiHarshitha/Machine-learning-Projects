# Diabetes Prediction Web App

A machine learning-based web application that predicts whether a person is diabetic or not using health-related input parameters. The application is built using Python, Streamlit, and a trained Machine Learning model.

---

## 📌 Features

- Predicts diabetes based on user health data
- Simple and interactive web interface using Streamlit
- Uses a trained Machine Learning model
- Scales input data before prediction
- Instant prediction results

---

## 🛠️ Technologies Used

- Python
- Streamlit
- NumPy
- Scikit-learn
- Pickle

---

## 📂 Project Structure

```bash
├── Diabetes web app prediction.py   # Streamlit web application
├── predictivesys.py                 # Testing prediction script
├── diabetes.csv                     # Dataset used for training
├── trained_model.sav                # Saved ML model
├── scaler.sav                       # Saved scaler object
└── README.md                        # Project documentation
```

---

## 📊 Input Features

The model predicts diabetes using the following inputs:

1. Pregnancies
2. Glucose Level
3. Blood Pressure
4. Skin Thickness
5. Insulin Level
6. BMI
7. Diabetes Pedigree Function
8. Age

---

## 🚀 How to Run the Project

### 1️⃣ Install Required Libraries

```bash
pip install numpy streamlit scikit-learn
```

### 2️⃣ Run the Streamlit App

```bash
streamlit run "Diabetes web app prediction.py"
```

---

## 🧠 Machine Learning Workflow

- Dataset loaded from `diabetes.csv`
- Data preprocessing and scaling applied
- Model trained using Scikit-learn
- Trained model saved as `trained_model.sav`
- Scaler saved as `scaler.sav`
- Streamlit app loads both files for prediction

---

## 📷 Application Preview

The web app allows users to:

- Enter medical details
- Click on **"Diabetes Test Result"**
- Get instant prediction output

---

## 📌 Example Prediction

```python
Input:
(4,110,92,0,0,37.6,0.191,30)

Output:
The person is NOT diabetic
```

---

## ⚠️ Note

This project is developed for educational and learning purposes only. It should not be used as a replacement for professional medical diagnosis.

---

## 👨‍💻 Author

Developed by Akhil / Harshitha Sandadi
