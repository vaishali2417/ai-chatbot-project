import json
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1) Load JSON file
with open("intents.json", "r") as f:
    data = json.load(f)

# 2) Extract patterns and tags
patterns = []
tags = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])

# 3) Convert to vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)

# 4) Train model
model = MultinomialNB()
model.fit(X, tags)

# 5) Save model + vectorizer + data
pickle.dump({
    "model": model,
    "vectorizer": vectorizer,
    "data": data
}, open("model.pkl", "wb"))

print("Model trained successfully!")
