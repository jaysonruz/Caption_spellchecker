import os
import requests
import json
from dotenv import load_dotenv



def bing_spellcheck(example_text):
    load_dotenv()
    # example_text = text # "Hollo, wrld" # the text to be spell-checked
    api_key = os.getenv('BING_API_KEY')
    url = "https://bing-spell-check2.p.rapidapi.com/spellcheck"

    querystring = {"mode":"proof","text":example_text}

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "bing-spell-check2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    # print(response.json())
    return response

if __name__ == "__main__":
    text = """ Reliance digital PERSsONALISING Technology A flip better than cars in Rohit Shetty's flicks an lost art."""
    print(bing_spellcheck(text).json())