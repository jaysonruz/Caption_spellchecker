#!/usr/bin/env python
# coding: utf-8

# In[1]:


# %pip install pandas
# %pip install gingerit
# %pip install regex
# %pip install openpyxl
#pip install Flask

import pandas as pd
import regex as re
from gingerit.gingerit import GingerIt


def remove_emoticons_hashtags_tags(text):
    # Remove emoticons
    text = re.sub(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U00002702-\U000027B0\U000024C2-\U0001F251]+', '', text)

    # Remove hashtags and @tags
#     text = re.sub(r'[@#]\w+', '', text)
# The pattern [#@]\S+\s will find words that start with @ or # and continue until a space is found in the given text. 
#  It will capture the entire word along with any special characters until the space is reached.
    text +=" "
    text = re.sub(r'[#@]\S+\s', '', text)

    # Remove anything inside parentheses
    text = re.sub(r'\([^)]*\)', '', text)
    
    # Remove any trailing punctuations
    text = text.replace("@","").replace("#","")
    
    return text.strip()

def check_correction_type(correction):
    excluded_correction_types = ['Accept space','Accept comma addition','None']
    for correction in ginger_cap['corrections']:
        print("\t ------------------",correction['definition'])
        if correction['definition'] in excluded_correction_types:
            return False
    return True

def fix_my_cap(text):
    parser = GingerIt()
    return parser.parse(remove_emoticons_hashtags_tags(text))

if __name__ == "__main__":
    text= """Gamers or hustlers. Corporate warriors or students. Whatever be their trip, what trips them up is a laptop that just cannot keep pace. #NewWork for @reliance_digital as part of “The Hunt for India’s Slowest Laptop” campaign by Team 21N.

Credits:
Brand: @reliance_digital
Client: Manoj Jain, Nisha Kallianpur, Anamika Tiwari, Esha Nath
Production House: @firsttakefilms
Direction: @sagnik6285
Creative Team: @bingeljell, @inde.stagram, @_kashishkakkar_
Account Management: @neerajkarkera , @divya_jain_dj, @aarsha_rathi
Founder & CEO: @the.malayali"""
    
    result = fix_my_cap(text)
    print(result)
