import nltk
import random
import spacy

nltk.download('punkt')
nltk.download('wordnet')

nlp=spacy.load('en_core_web_sm')

Greeting_msg=("hello","hi","greetings","namaste","sup","what's up", "hey")
Greeting_reply=["hi","hey","hello","I am glad! You are talking to me","namaste"]
Farewell_msg=("bye","see you", "goodbye", "later", "goodbye")
Farewell_reply=["bye","take care","see you later","goodbye"]

def greet(sentence):
    for word in sentence.split():
        if word.lower() in Greeting_msg:
            return random.choice(Greeting_reply)
        

def farewell(sentence):
    for word in sentence.split():
        if word.lower() in Farewell_msg:
            return random.choice(Farewell_reply)

def chatbot_response(user_input):
    user_input = user_input.lower()

    if greet(user_input) is not None:
        return greet(user_input)
    if farewell(user_input) is not None:
        return farewell(user_input)
    
    document =nlp(user_input)
    tokens= [token.text for token in document]

    if "weather" in tokens:
        return " The weather is nice today!! Some chances of rain later!!"
    elif "name" in tokens:
        return "My name is Code Alpha's chatbot. What's yours?"
    elif "internship" in tokens:
        return "We rpovide internship in various domains such  Python programming, Web designing, Data science etc..."
    elif "help" in tokens:
        return "You can get some help using our Whatsapp Number and talk to expert.."
    else:
        return " I am sorry! i don't understand you."
    
def main():
    print("Hi! I'm a chatbot. How can I help you?")
    while True:
        user_input = input()
        if user_input.lower() in Farewell_msg:
            print(farewell(user_input))
            break
        print(chatbot_response(user_input))

if __name__ == "__main__":
    main()