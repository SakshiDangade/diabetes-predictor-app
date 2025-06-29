# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 22:12:47 2025

@author: saksh
"""

import numpy as np
import pickle 
import streamlit as st

loaded_model=pickle.load(open('trained_model.sav', 'rb'))

def diabetes_prediction(input_data):
    
    input_data_as_numpy_array=np.asarray(input_data)

    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    
def main():
    
    st.title('Diabetes Prediction Web App')
    
    
    Pregnancies=st.text_input("Number of Pregnancies")
    Glucose=st.text_input("Glucose Level")
    BloodPressure=st.text_input("Blood Pressure Value")
    SkinThickness=st.text_input("Skin Thickness Value")
    Insulin=st.text_input("Insulin Level")
    BMI=st.text_input("BMI Value")
    DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function Value")
    Age=st.text_input("Age of the person")
    
    diagnosis=''
    
    if st.button("Diabetes Test Result"):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    
    
if __name__=="__main__":
    main()
    
    
    