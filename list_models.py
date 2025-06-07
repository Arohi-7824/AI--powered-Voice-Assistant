import google.generativeai as genai

# Replace with your actual Gemini API key
genai.configure(api_key="AIzaSyC4UxcOfdNMocqPialOHs8p3zw7PMJhYv0")

# List and print available models
for model in genai.list_models():
    print(model.name)
