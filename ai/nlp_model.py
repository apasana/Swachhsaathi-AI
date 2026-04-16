import re
import string

STOPWORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for', 'if', 'in',
    'into', 'is', 'it', 'no', 'not', 'of', 'on', 'or', 'such', 'that', 'the',
    'their', 'then', 'there', 'these', 'they', 'this', 'to', 'was', 'will', 'with'
}


def analyze_complaint(text):
    # Preprocess text with a simple tokenizer
    clean_text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text.lower())
    tokens = [word for word in clean_text.split() if word not in STOPWORDS and word not in string.punctuation]

    # Rule-based classification
    if 'missed' in tokens or 'nahi' in tokens and 'aaya' in tokens or 'pickup' in tokens:
        category = 'Missed Pickup'
        priority = 'High'
    elif 'overflow' in tokens or 'full' in tokens or 'bhara' in text.lower():
        category = 'Overflow'
        priority = 'Medium'
    else:
        category = 'General'
        priority = 'Low'

    return category, priority