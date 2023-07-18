import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from src.main import tasks
from src.logger import logging
from src.exception import CustomException


# Create the application
st.title("Text Solution")
st.write('Text Solution lets you summarize, analyze sentiment and compare semantic similarity of texts.')

tab1, tab2= st.tabs(["Home", "Text Similarity"])


# Create the home tab with two features summerize and get_sentiment
with tab1:  
    user_input = st.text_area(label="Enter the text.")
    
    # Create summarization button
    with st.spinner('Summarizing...'):      # adds loading spinner
        if st.button(label="Summarize Text"):  # raise error if textbox is empty
            if user_input=='':
                st.error('Please enter a text.')
            else:
                result = tasks.summarize(text=user_input)
                st.success('Done!')
                st.write(result)

    # Create get_sentiment
    with st.spinner('Analyzing...'):
        if st.button(label="Get Sentiment"):
            if user_input=='':
                st.error('Please enter a text')
            else:
                result = tasks.get_sentiment(text=user_input)
                st.success('Done')
                st.write(result)

    

with tab2:
    user_input1 = st.text_area(label="Enter your text.")
    user_input2 = st.text_area(label="Enter the second text.")
    with st.spinner('Comparing...'):
        if st.button(label="Get Similarity Score"):
            if user_input1=='' or user_input2=='':
                st.error('Please enter both the texts.')
            else:
                result = tasks.get_similarity(text1=user_input1, text2=user_input2)
                st.success('Done')
                st.write('These two sentences are',result,'% similar.')
    
