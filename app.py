from flask import Flask, request, jsonify, send_file
from caption_fixer import fix_my_cap,remove_emoticons_hashtags_tags
from textgear_spellcheck import textgear_spellcheck
from bingspell import bing_spellcheck
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
            # show below results parallelly 
            full_result={}
            result1 = fix_my_cap(text)
            result2 = bing_spellcheck(text).json()
            result3 = textgear_spellcheck(text).json()
            cleaned_text = remove_emoticons_hashtags_tags(text)
            
            full_result['cleaned_text']=cleaned_text
            full_result['Gingerit']=result1
            full_result['Bing API']=result2
            full_result['Textgear API']=result3
            
            return jsonify(full_result)
        else:
            return jsonify({"error": "Invalid input. 'text' parameter is missing."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
