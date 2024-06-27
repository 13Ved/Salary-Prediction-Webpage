# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:50:55 2024

@author: VEDSD
"""

import streamlit as st
import pickle 
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data= load_model()

Regressor = data["model"]
Encode_Industry = data["Encode_Industry"]
Encode_Age = data["Encode_Age"]
Encode_Work = data["Encode_Work"]
Encode_Country = data["Encode_Country"]
Encode_Ed = data["Encode_Ed"]

def show_predict_page():
    st.title("Salary Prediction of an Employee")
    
    st.write("""We need some information to Predict the Salary""")
    

    Industry=('Advertising Services',
              'Financial Services',
              'Healthcare',
              'Information Services, IT, Software Development, or other Technology',
              'Insurance',
              'Legal Services',
              'Manufacturing, Transportation, or Supply Chain',
              'Oil & Gas',
              'Retail and Consumer Services',
              'Wholesale',
              'Other'
        )
    
    Age=('18-24 years old',
         '25-34 years old', 
         '45-54 years old', 
         '35-44 years old',
         '55-64 years old', 
         '65 years or older'
        )
    
    Workspace=('Remote', 
               'Hybrid', 
               'In-person'
        )
    
    Countries=("Other",                                                   
    "United States of America",                                
    'Germany',                                                  
    'United Kingdom of Great Britain and Northern Ireland',     
    'Canada',                                                   
    'India',                                                   
    'France' ,                                                 
    'Netherlands',                                              
    'Australia'  ,                                                   
    'Spain'      ,                                              
    'Brazil'     ,                                              
    'Sweden'     ,                                               
    'Italy'      ,                                               
    'Poland'     ,                                               
    'Switzerland')
    
    
    
    Education=('Less than a Bachelors',
               'Bachelor’s degree',
               'Master’s degree',
               'Post grad'
        )
    
    
    Industry= st.selectbox("Industry",Industry)
    Age_Category= st.selectbox("Age Category",Age)
    Workspace= st.selectbox("Workspace",Workspace)
    Country= st.selectbox("Country",Countries)
    Education= st.selectbox("Education level",Education)
    experience=st.slider("Years of Working Experience",0,50)
    
    Ok=st.button("Predict Salary")
    if Ok:
        X_sub = np.array([[Industry,Age_Category,Workspace,experience,Country,Education ]])
        
        X_sub[:, 0] = Encode_Industry.transform(X_sub[:,0])
        X_sub[:, 1] = Encode_Age.transform(X_sub[:,1])
        X_sub[:, 2] = Encode_Work.transform(X_sub[:,2])
        X_sub[:, 4] = Encode_Country.transform(X_sub[:,4])
        X_sub[:, 5] = Encode_Ed.transform(X_sub[:,5])
        X_sub = X_sub.astype(float)
        
        salary=Regressor.predict(X_sub)
        st.subheader(f'The estimated salary in USD is ${salary[0]:.2f}')
        