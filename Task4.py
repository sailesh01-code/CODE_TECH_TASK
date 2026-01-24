#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# In[4]:
import pandas as pd

url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"

data = pd.read_csv(
    url,
    sep='\t',
    header=None,
    names=['label', 'message']
)
data.head()


# In[5]:


# Convert labels to binary
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Split features and labels
X = data['message']
y = data['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


# In[6]:


model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('classifier', MultinomialNB())
])


# In[7]:


model.fit(X_train, y_train)


# In[8]:


# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Confusion Matrix
print("Confusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))


# In[9]:


sample_emails = [
    "Congratulations! You've won a free iPhone. Click now!",
    "Hey, are we still meeting for lunch today?",
    "Limited time offer!!! Get cheap loans now"
]

predictions = model.predict(sample_emails)

for email, label in zip(sample_emails, predictions):
    print(f"Email: {email}")
    print("Prediction:", "Spam" if label == 1 else "Not Spam")
    print("-" * 50)


# In[ ]:




