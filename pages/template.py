import streamlit as st
import pandas as pd
import json
import os

with open('setting.json', 'r', encoding="UTF-8") as json_open:
    SETTING = json.load(json_open,)
with open('articles.json','r', encoding="UTF-8") as article_open:
    ARTICLE = json.load(article_open)

name = "日本国憲法"
text = ARTICLE[name]["前文"]['text']
st.title("前文")
st.markdown(f'{text}')