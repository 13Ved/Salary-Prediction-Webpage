# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:52:50 2024

@author: VEDSD
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

def Change_Cat(categories,limit):
    categorical_map={}
    for i in range(len(categories)):
        if categories.values[i]>=limit:
            categorical_map[categories.index[i]]=categories.index[i]
        else:
            categorical_map[categories.index[i]]='Other'
    return categorical_map

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'

def clean_WorkEN(x):
    if 'Hybrid' in x:
        return 'Hybrid'
    else:
        return x

def clean_Age(x):
    if 'Prefer not to say' in x:
        return '25-34 years old'
    if 'Under 18 years old' in x:
        return '18-24 years old' 
    else:
        return x
    
@st.cache_data 
def load_data():
    Data=pd.read_csv('C:\\Users\\VEDSD\\Project\\Salary Prediction\\stack-overflow-developer-survey-2023\\survey_results_public.csv')
    df=Data[['Industry','ConvertedCompYearly','Age','RemoteWork','WorkExp','Employment','Country','EdLevel']]
    
    df=df.dropna(subset=['ConvertedCompYearly','Employment','RemoteWork','Country'])
    
    df['Industry']=np.where(df['Industry'].isnull()==True,'I[nformation Services, IT, Software Development, or other Technology',df['Industry'])
    df['WorkExp']=np.where(df['WorkExp'].isnull()==True,np.mean(df['WorkExp']),df['WorkExp'])
 
    df=df[df['Employment']=='Employed, full-time']
    df=df.drop('Employment',axis=1)
    
    country_map=Change_Cat(df.Country.value_counts(),500)
    df['Country']=df['Country'].map(country_map)
    
    df=df.rename(columns = {'ConvertedCompYearly':'Salary'})
    
    df=df[df['Salary']<=(1000000*0.4)]
    df=df[df['Salary']>10000] 
    
    df['Industry']=np.where(df['Industry']=='I[nformation Services, IT, Software Development, or other Technology',
                       'Information Services, IT, Software Development, or other Technology',df['Industry'])

    df['EdLevel'] = df['EdLevel'].apply(clean_education)
    
    df['RemoteWork']=df['RemoteWork'].apply(clean_WorkEN)
    
    return df
    
df=load_data()

def show_explore_page():        
    st.title("Explore Salary of an Employee")
        
    st.write(""" 
             #### From Survey taken by Stack Overflow 2023
             
            """)
        
    data=df['Country'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=40)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Number of Data from different countries""")

    st.pyplot(fig1)    
    
    st.write(
        """
    #### Mean Salary Based On Country
    """
    )

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)
    
    st.write(
        """
    #### Median Salary Based On Experience
    """
    )

    data = df.groupby(["WorkExp"])["Salary"].median().sort_values(ascending=True)
    st.line_chart(data)
    
    st.write(
        """
    #### Mean Salary Based On Industry
    """
    )
    
    data = df.groupby(["Industry"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)
    
    st.write(
        """
    #### Median Salary Based On Education
    """
    )
    
    data = df.groupby(["EdLevel"])["Salary"].median()
    st.bar_chart(data)
    
    st.write(
        """
    #### Workspace count Based on Industry
    """
    )
    
    data = df.groupby(["Industry","RemoteWork"]).size().unstack(fill_value=0)
    st.bar_chart(data)
    
    st.write(
        """
    #### Education level count Based on Industry
    """
    )
    
    data = df.groupby(["Industry","EdLevel"]).size().unstack(fill_value=0)
    st.bar_chart(data)
    st.bar_chart()