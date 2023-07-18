Welcome to Text Solution!

A streamlit application built in Python to summarize, analyze sentiment and compare the semantic similarity of texts.

The application has three features:
  1. Summarizes the given text.
  2. Analyze the sentiment of the given text (shows how positive, neutral or negative the sentence is).
  3. Compares and gives a similarity score between two given texts (sentences or paragraphs).

All three features use the Hugging Face 🤗 transformers' NLP models.

* The summarization feature uses the [BART large CNN model](https://huggingface.co/facebook/bart-large-cnn) via Inference API to generate text summary.
* The sentiment analyzer fetches the [Twitter Roberta Base Sentiment Latest model](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) via Inference API.
* The Text Similarity feature uses [All mpnet base v2 model](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) to encode the user input sentences and a similarity score is given based on cosine similarity. 
