from flask import Flask, render_template, request, jsonify
from assistant import get_gemini_response  # Your backend logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/message', methods=['POST'])
def get_response():
    data = request.json
    user_input = data.get('message', '')
    
    # Pass user input to your Gemini response function
    response = get_gemini_response(user_input)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
