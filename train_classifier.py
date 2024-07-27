import spacy
import nltk
from nltk.classify import NaiveBayesClassifier
from sklearn.model_selection import train_test_split
import pickle
import csv

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to preprocess text
def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.text for token in doc if not token.is_stop and token.is_alpha]
    return tokens

# Function to extract features
def extract_features(words):
    return {word: True for word in words}

# Load the dataset
data = []
with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header
    for row in reader:
        description, label = row
        data.append((description, label))

# Preprocess the dataset
dataset = [(extract_features(preprocess(description)), label) for description, label in data]

# Split the dataset
train_data, test_data = train_test_split(dataset, test_size=0.2)

# Train the classifier
classifier = NaiveBayesClassifier.train(train_data)

# Save the trained classifier
with open('classifier_model.pkl', 'wb') as f:
    pickle.dump(classifier, f)

# Evaluate the classifier
accuracy = nltk.classify.accuracy(classifier, test_data)
print(f'Accuracy: {accuracy * 100:.2f}%')
