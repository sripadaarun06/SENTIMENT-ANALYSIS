import pandas as pd
import numpy as numpy
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import multinomialNB
from sklearn.metrics import classification_report, confusion_matrix
