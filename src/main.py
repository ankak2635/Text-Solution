import sys
from src.exception import CustomException
from src.logger import logging
# import APIconfig uncomment for local run

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import requests

class tasks:
    def __init__(self):
        pass

# Create summerization task
    def summarize(text:str):
        logging.info("Entered the summerizer")

        try:
            API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
            # headers = {"Authorization": APIconfig.token}
            headers = {"Authorization": st.secrets['token']}  #for deployment

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()
            
            summary = query(text)
            summary= pd.DataFrame(summary)
            summary= summary['summary_text'][0]

            return summary
	
        except Exception as e:
            raise CustomException(e,sys)
        

    # Create get_sentiment task
    def get_sentiment(text:str):
        logging.info("Entered the get_sentiment function")
        try:
            API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
            # headers = {"Authorization": APIconfig.token}
            headers = {"Authorization": st.secrets['token']}  #for deployment

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()
            
            sentiment = query(text)
            sentiment_res = pd.DataFrame(sentiment).T
            sentiment_res= sentiment_res[0].apply(pd.Series)

            #Make a piechart of the results
            fig1= plt.figure(figsize=(5,5))
            plt.pie(sentiment_res.score, labels=sentiment_res.label, autopct='%.0f%%', 
                    explode=(0.1, 0, 0), shadow=False, startangle=90)

            return fig1 #return a pie plot

        except:
            pass

    # Create get_similarity task
    def get_similarity(text1, text2):
        logging.info('Entered the similarity function')
        try:
            model = SentenceTransformer('all-mpnet-base-v2')
            texts = [text1, text2]
            embeddings = model.encode(texts)
            slimilarity = cosine_similarity([embeddings[0]], embeddings[1:])

            # Format the answer
            slimilarity = pd.DataFrame(slimilarity)
            slimilarity[0] = slimilarity[0]*100
            slimilarity = round(slimilarity[0][0])
            slimilarity = str(slimilarity)
            return slimilarity
        
        except Exception as e:
            raise CustomException(e,sys)
        


    
            
