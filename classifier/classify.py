import spacy
import nltk
import pickle

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

# Load the trained classifier
# with open('/home/IIF/classifier_model.pkl', 'rb') as f: use this line if you want to run the app on a server
with open('classifier_model.pkl', 'rb') as f:
    classifier = pickle.load(f)

# Function to classify a new description
def classify_description(description):
    tokens = preprocess(description)
    features = extract_features(tokens)
    return classifier.classify(features)

import pickle

# Save the classifier
# with open('/home/IIF/classifier_model.pkl', 'wb') as f: use this line if you want to run the app on a server
with open('classifier_model.pkl', 'wb') as f:
    pickle.dump(classifier, f)
