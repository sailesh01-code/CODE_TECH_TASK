import nltk
import random
import string
from nltk.chat.util import Chat, reflections
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Chat patterns (intents and responses)
pairs = [
    [
        r"(hi|hello|hey)",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I am an AI Chatbot created using Python and NLP."]
    ],
    [
        r"how are you ?",
        ["I'm doing great! How about you?"]
    ],
    [
        r"(what can you do|help)",
        ["I can answer simple questions using NLP."]
    ],
    [
        r"(bye|exit|quit)",
        ["Goodbye! Have a great day 😊"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you rephrase?"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return tokens

def start_chat():
    print("🤖 AI Chatbot (type 'bye' to exit)")
    print("---------------------------------")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! 👋")
            break
        
        response = chatbot.respond(user_input)
        print("Bot:", response)

# Run chatbot
start_chat()
