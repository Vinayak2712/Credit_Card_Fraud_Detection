# importing all the required libraries to create WEB APP

import streamlit as st
import pickle
from streamlit_option_menu import option_menu

#loading the model 
fraud_detection_model = pickle.load(open("D:\work\Fraud Detection\Fraud_Detection (1).sav", 'rb'))

#creating the side bar
with st.sidebar:
    selected = option_menu("Created by -  Vinayak Shivanagutti",
                            ['Credit Card Fraud Detection System'])

if (selected == 'Credit Card Fraud Detection System'):
    
    st.title("Fraud transactions Detected using ML")
    
    col1,col2,col3,col4,col5,col6,col7 = st.columns(7)
    
    with col1:
        V1 = st.text_input("Enter V1 value ")
        
    with col2:
        V2 = st.text_input("Enter V2 value ")
        
    with col3:
        V3 = st.text_input("Enter V3 value ")
    with col4:
        V4 = st.text_input("Enter V4 value ")
    with col5:
        V5 = st.text_input("Enter V5 value ")
    with col6:
        V6 = st.text_input("Enter V6 value ")
    with col7:
        V7 = st.text_input("Enter V7 value ")
    with col1:
        V8 = st.text_input("Enter V8 value ")
    with col2:
        V9 = st.text_input("Enter V9 value ")
    with col3:
        V10 = st.text_input("Enter V10 value ")
    with col4:
        V11 = st.text_input("Enter V11 value ")
    with col5:
        V12 = st.text_input("Enter V12 value ")
    with col6:
        V13 = st.text_input("Enter V13 value ")
    with col7:
        V14 = st.text_input("Enter V14 value ")
    with col1:
        V15 = st.text_input("Enter V15 value ")
    with col2:
        V16 = st.text_input("Enter V16 value ")
    with col3:
        V17 = st.text_input("Enter V17 value ")
    with col4:
        V18 = st.text_input("Enter V18 value ")
    with col5:
        V19 = st.text_input("Enter V19 value ")
    with col6:
        V20 = st.text_input("Enter V20 value ")
    with col7:
        V21 = st.text_input("Enter V21 value ")
    with col1:
        V22 = st.text_input("Enter V22 value ")
    with col2:
        V23 = st.text_input("Enter V23 value ")
    with col3:
        V24 = st.text_input("EnterV24 value ")
    with col4:
        V25 = st.text_input("Enter V25 value ")
    with col5:
        V26 = st.text_input("Enter V26 value ")
    with col6:
        V27 = st.text_input("Enter V27 value ")
    with col7:
        V28 = st.text_input("Enter V28 value ")
    
    
    fraud_detection = ""
    
    if st.button("Detect the Transaction"):
        detection = fraud_detection_model.predict([[V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28]])
        
        if (detection[0]==1):
            fraud_detection = "ALERT.! It's FRAUD Transaction"
        else:
            fraud_detection = "SAFE transaction"
   

