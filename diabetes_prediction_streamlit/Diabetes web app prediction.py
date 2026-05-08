# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:29:06 2026

@author: akhil
"""
import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('D:\python_ml\ml_projects\deploying ml model\\trained_model.sav','rb'))

scaler = pickle.load(open('D:\python_ml\ml_projects\deploying ml model\\scaler.sav', 'rb'))

#creating a function for diabetes prediction
def diabetes_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)

    # Apply SAME scaler
    input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)
    input_scaled =scaler.transform(input_data_reshaped)
    prediction = loaded_model.predict(input_scaled)
    print(prediction)

    if prediction[0] == 0:
        return "The person is NOT diabetic"
    else:
        return "The person is diabetic"

def main():
    #giving a title
    st.title("Diabetes Prediction Web APP")
    
    #getting the input data from the user
    Pregnancies = st.number_input("Number of Pregnancies")
    Glucose= st.number_input("Glucose Level")
    BloodPressure= st.number_input("Blood Pressure value")
    SkinThickness= st.number_input("Skin Thickness value")
    Insulin= st.number_input("Insulin Level")
    BMI= st.number_input("BMI value")
    DiabetesPedigreeFunction=st.number_input("Diabetes Pedigree Function value")
    Age = st.number_input("Age")
    
    #code for prediction
    diagnosis=''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
       diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    
    
if __name__=='__main__':
    main()
