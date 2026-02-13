# Physics Educational Chatbot

A simple, interactive, terminal-based Python chatbot designed to help users learn about core physics topics: **Mechanics**, **Optics**, and **Thermodynamics**.

The bot uses a pattern-matching approach to understand user input and features a guided conversation loop that remembers the current topic being discussed.

## Features
* **Guided Dialogue:** The bot remembers the topic you select (state-tracking) and offers specific sub-categories (Overview, Definition, Laws, Scientist info) to guide your learning.
* **Text Preprocessing:** Automatically handles user input by converting it to lowercase and stripping punctuation, making the bot more forgiving of typos and formatting.
* **JSON-Driven Responses:** All intents, patterns, and responses are cleanly separated into an `intents.json` file, making it incredibly easy to add new topics or modify the bot's dialogue without touching the Python logic.
* **Zero External Dependencies:** Built entirely using Python's standard library.

## Project Structure
* `chatbot.py`: The main script containing the logic for text preprocessing, intent matching, and the interactive conversation loop.
* `intents.json`: The data file containing the predefined tags, user input patterns, and bot responses.

## Prerequisites
You only need **Python 3.x** installed on your system. Because this project relies entirely on built-in Python modules (`json`, `string`, `random`), there is no need to install anything via `pip`.

## How to Run

1. Clone or download this repository.
2. Ensure both `chatbot.py` and `intents.json` are in the same directory.
3. Open your terminal or command prompt.
4. Navigate to the project directory.
5. Run the script:
   ```bash
   python chatbot.py
Bot: Hi! I am your Physics Chatbot. Ask me about Mechanics, Optics, or Thermodynamics.

You: mechanics

Bot: Great choice! What would you like to know about this topic?
1. Overview
2. Definition
3. Laws
4. Scientist info

You: laws

Bot: The fundamental laws of mechanics are Newton's three laws of motion: the law of inertia, the law of acceleration, and the law of action and reaction.

Do you want to continue with Mechanics or choose another topic?
You: no
Bot: Okay, which topic do you want to choose? Mechanics, Optics, or Thermodynamics?
Customization
To add new subjects or responses, simply open intents.json and add a new dictionary object to the "intents" list following the existing structure. Update the topic_intent_map in chatbot.py if you are adding an entirely new branch of physics.