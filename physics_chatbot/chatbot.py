import json
import string
import random

with open("intents.json") as file:
    data = json.load(file)

data["intents"]     # is a list of intents.

# Step 3 Text Preprocessing (Very Important)
# Computers can’t handle raw text well.
# So we normalize it.

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

# .lower() → removes case differences
# .translate() → removes punctuation

# Step 4️ Intent Matching Logic 

def get_intent(user_input):
    user_input = preprocess(user_input)

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern = preprocess(pattern)
            if pattern in user_input:
                return intent["tag"]

    return "unknown"

# Step 5️ RESPONSE FUNCTION

def get_response(intent_tag):
    for intent in data["intents"]:
        if intent["tag"] == intent_tag:
            # Pick a random response if multiple
            return random.choice(intent["responses"])
    # Fallback if intent not found
    return "Sorry, I didn't understand that."

# Step 6 Main Chat Loop

print("Bot: Hi! I am your Physics Chatbot. Ask me about Mechanics, Optics, or Thermodynamics.")

current_topic = None  # <-- Step 1: topic memory

while True:
    user = input("You: ").strip()

    if user == "":
        continue  # ignore blank input

    if user.lower() in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! See you next time.")
        break

    if user.lower() in ["yes", "y"]:
        print("Bot: What would you like to know about", current_topic.capitalize(), "?")
        print("1. Overview\n2. Definition\n3. Laws\n4. Scientist info")
        continue

    if user.lower() in ["no", "n"]:
        current_topic = None
        print("Bot: Okay, which topic do you want to choose? Mechanics, Optics, or Thermodynamics?")
        continue

    # Step 3: Check if user is selecting a topic
    if user.lower() in ["mechanics", "optics", "thermodynamics"]:
        current_topic = user.lower()
        print("Bot: Great choice! What would you like to know about this topic?")
        print("1. Overview\n2. Definition\n3. Laws\n4. Scientist info")
        continue  # wait for next input

    # Step 4: Guided question based on topic
    if current_topic:
        # Map user input to intent tag
        topic_intent_map = {
            "overview": f"{current_topic}_overview",
            "definition": f"{current_topic}_definition",
            "laws": f"{current_topic}_laws",
            "law": f"{current_topic}_laws",       # accept singular too
            "scientist": f"{current_topic}_facts",
            "who": f"{current_topic}_facts" ,     # accept 'who' for scientist
        }

        key = user.lower()
        if key in topic_intent_map:
            intent_tag = topic_intent_map[key]
            response = get_response(intent_tag)
            print("Bot:", response)
            print("\nDo you want to continue with", current_topic.capitalize(), "or choose another topic?")
            continue
        else:
            print("Bot: Sorry, I didn't understand. Please choose Overview, Definition, Laws, or Scientist info.")
            continue

    # Step 5: General intents (like greeting)
    intent = get_intent(user)
    response = get_response(intent)
    print("Bot:", response)
