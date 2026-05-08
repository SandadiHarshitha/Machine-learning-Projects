# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

#loading the saved model
loaded_model=pickle.load(open('D:\python_ml\ml_projects\deploying ml model\\trained_model.sav','rb'))

scaler = pickle.load(open('D:\python_ml\ml_projects\deploying ml model\\scaler.sav', 'rb'))

input_data = (
4,110,92,0,0,37.6,0.191,30)

input_data_as_numpy_array = np.asarray(input_data)

# Apply SAME scaler
input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)
input_scaled =scaler.transform(input_data_reshaped)
prediction = loaded_model.predict(input_scaled)
print(prediction)

if prediction[0] == 0:
    print("The person is NOT diabetic")
else:
    print("The person is diabetic")