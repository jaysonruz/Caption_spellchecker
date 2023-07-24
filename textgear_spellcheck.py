import requests
import os
from dotenv import load_dotenv

def textgear_spellcheck(text):
	load_dotenv()
	api_key = os.getenv('TEXTGEAR-API-KEY')

	url = "https://textgears-textgears-v1.p.rapidapi.com/grammar"

	payload = { "text": text }
	headers = {
		"content-type": "application/x-www-form-urlencoded",
		"X-RapidAPI-Key": api_key,
		"X-RapidAPI-Host": "textgears-textgears-v1.p.rapidapi.com"
	}

	response = requests.post(url, data=payload, headers=headers)
	return response


if __name__ == "__main__":
    text = """ Reliance digital PERSsONALISING Technology A flip better than cars in Rohit Shetty's flicks an lost art."""
    print(textgear_spellcheck(text).json())