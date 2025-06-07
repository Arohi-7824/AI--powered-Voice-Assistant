import google.generativeai as genai
from .config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

# Recommended model as of 2025

model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

def get_gemini_response(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
