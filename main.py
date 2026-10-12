import os
from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)

ai = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
            
        response = ai.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_message,
        )
        
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
