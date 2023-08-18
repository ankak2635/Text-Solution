# Welcome to Text Solution!

Thank you for exploring Text Solution, a Python-based Streamlit application designed to provide text summarization, sentiment analysis, and semantic similarity comparison for texts.

🔗 **Explore the application [here.](https://text-solution-2635.streamlit.app/)**

## Features

Text Solution offers three distinct features:

1. **Text Summarization**: Efficiently summarizes provided texts using the [BART large CNN model](https://huggingface.co/facebook/bart-large-cnn) through the Inference API.

2. **Sentiment Analysis**: Assesses sentiment in given texts, displaying the degree of positivity, neutrality, or negativity. This functionality is supported by the [Twitter Roberta Base Sentiment Latest model](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) via the Inference API.

3. **Text Similarity Comparison**: Measures semantic similarity between two input texts, whether they are sentences or paragraphs. This comparison is facilitated by the [all- mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) model, producing a similarity score based on cosine similarity.

## Leveraging Hugging Face NLP Models

Text Solution harnesses the power of Hugging Face's 🤗 transformers' NLP models to offer accurate and sophisticated text analysis.

- The summarization feature employs the BART Large CNN model via the Inference API to generate concise text summaries.
- Sentiment analysis utilizes the Twitter Roberta Base Sentiment Latest model through the Inference API to assess text sentiment.
- Text similarity comparison relies on the All mpnet Base v2 model to encode user-input sentences, ultimately deriving a similarity score using cosine similarity.

## Getting Started

To get started with Text Solution, follow the link to the application and experience the capabilities firsthand.

Thank you for your interest in Text Solution!
