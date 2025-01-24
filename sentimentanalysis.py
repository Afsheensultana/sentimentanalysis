# -*- coding: utf-8 -*-
"""sentimentanalysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13FYF7Rj6JBbp_0Q0492zs-qC4hK6SpLE
"""

# Importing necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import re

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load your dataset (replace the file path with your actual file)
df = pd.read_csv("https://github.com/suhasmaddali/Twitter-Sentiment-Analysis/raw/refs/heads/main/train.csv")

# Ensure all non-string values are handled
df['selected_text'] = df['selected_text'].fillna('').astype(str)

# Step 1: Cleaning the text
cleaned = []
for text in df['selected_text']:
    cleaned_text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation and special characters
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Replace multiple spaces with a single space
    cleaned.append(cleaned_text.strip())  # Strip leading/trailing spaces

# Step 2: Tokenizing the cleaned text
tokens = [word_tokenize(x) for x in cleaned]

# Step 3: Removing stopwords
stop = set(stopwords.words('english'))
stpktn = [[word for word in sentence if word not in stop] for sentence in tokens]

# Step 4: Displaying results
print("Cleaned Text:", cleaned[:5])  # Display first 5 cleaned texts
print("Tokens:", tokens[:5])  # Display tokens for the first 5 cleaned texts
print("Tokens without Stopwords:", stpktn[:5])  # Display tokens without stopwords for the first 5 cleaned texts

# Import necessary libraries
import pandas as pd
import os

# Download the file from GitHub
!wget https://github.com/suhasmaddali/Twitter-Sentiment-Analysis/raw/refs/heads/main/train.csv -O train.csv

# Load the dataset into a Pandas DataFrame
df = pd.read_csv("train.csv")

from sklearn.feature_extraction.text import CountVectorizer

cv=CountVectorizer()

#importing multinomialnb
from sklearn.naive_bayes import MultinomialNB

print(df.columns)

y=df['selected_text']

y

mb= MultinomialNB()

from nltk.stem import PorterStemmer
ps=PorterStemmer()

ps.stem(df['selected_text'][0])

stemed_data=[]
 for message in stpktn:
  stem=[ps.stem(word) for word in message]
  stemed_data.append(stem)

stemed_data

stem_vec=[' '.join(message) for message in stemed_data]

stem_vec

x_vec=cv.fit_transform(stem_vec).toarray()

x_vec

len(x_vec[0])

y=df['sentiment']

y

mb= MultinomialNB()

mb.fit(x_vec,y)

x_vec[0]

df['selected_text'][0]

mb.predict([x_vec[0]])

#1- do train test split
#2-create a logistic regression model
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_vec,y,test_size=0.2)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)
y_pred=lr.predict(x_test[0].reshape(1,-1))
print(y_pred)

lr.score(x_test,y_test)

