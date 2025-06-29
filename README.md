# SENTIMENT-ANALYSIS
This project performs sentiment analysis on airline-related tweets using NLP techniques. The notebook includes data cleaning, text preprocessing, TF-IDF vectorization, and model building using Logistic Regression. Results are evaluated using accuracy, classification report, and confusion matrix.

COMPANY: CODTECH IT SOLUTIONS

NAME: SRIPADA ARUN

INTERN ID: CT08DF2529

DOMAIN: Data Analytics

MENTOR: NEELA SANTOSH


# Sentiment Analysis on Airline Tweets

This project applies **Natural Language Processing (NLP)** techniques to perform sentiment analysis on tweets related to major U.S. airlines. The goal is to classify tweets into **positive**, **neutral**, or **negative** sentiments.

---

## Dataset

The dataset used is `Tweets.csv`, which contains real tweets about airlines along with their associated sentiment labels.

### Key Columns:
- `text` - The tweet content
- `airline_sentiment` - Sentiment label (positive, neutral, negative)

---

## Task

Perform sentiment classification using the following pipeline:

1. **Text Preprocessing**  
   Cleaning, removing stopwords, and lemmatization

2. **Feature Extraction**  
   Using `TF-IDF` vectorizer to convert text to numerical form

3. **Model Training**  
   Logistic Regression classifier

4. **Evaluation**  
   Accuracy, classification report, and confusion matrix

---

## Results

- **Model Used:** Logistic Regression
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-score
- **Insights:**  
  - Majority of tweets are negative  
  - Misclassifications mostly happen between neutral and positive tweets
 
  - ![Image](https://github.com/user-attachments/assets/9d784332-ad7a-4762-b0f6-e3fa765d7c31)
  - ![Image](https://github.com/user-attachments/assets/78df002d-1695-4283-9758-5f21f511a173)

---

## Requirements

1. Python 3.x
2. pandas
3. numpy
4. scikit-learn
5. nltk
6. seaborn
7. matplotlib

---

## How to Run

1. Clone this repository  
2. Install the requirements  
3. Run the Jupyter notebook

```bash
pip install -r requirements.txt
jupyter notebook Sentiment_Analysis.ipynb
