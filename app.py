# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:51:54 2024

@author: VEDSD
"""

import streamlit as st
from Predict_Page import show_predict_page
from Explore import show_explore_page


page=st.sidebar.selectbox('Explore or Predict',("Predict","Explore"))
if page=='Predict':
    show_predict_page()
else:
    show_explore_page()
    

