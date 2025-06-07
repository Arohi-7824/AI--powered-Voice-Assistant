# AI Voice Assistant - Gemini

An AI voice assistant web application that enables natural, hands-free interactions using advanced speech recognition and synthesis. Powered by Google Gemini API, it provides intelligent, real-time responses to user queries.

## Features

- Speech-to-text voice input
- AI-powered conversational responses via Gemini API
- Text-to-speech synthesis for assistant replies
- Responsive web frontend built with Flask and JavaScript

## Setup Instructions

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/ai-voice-assistant.git
   cd ai-voice-assistant

2. Create and activate a Python virtual environment:

    ```bash

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

    ```bash

    pip install -r requirements.txt
    Add your Google Gemini API key in a .env file or config.py.

4. Run the Flask app:

    ```bash

    python app.py

5. Open your browser and visit http://localhost:5000.