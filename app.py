from flask import Flask, request, jsonify, send_file
from caption_fixer import fix_my_cap,remove_emoticons_hashtags_tags
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/fix_caption', methods=['POST'])
def fix_caption():
    try:
        data = request.get_json()
        if 'text' in data:
            text = data['text']
            result = fix_my_cap(text)
            cleaned_text = remove_emoticons_hashtags_tags(text)
            result['cleaned_text']=cleaned_text
            return jsonify(result)
        else:
            return jsonify({"error": "Invalid input. 'text' parameter is missing."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
