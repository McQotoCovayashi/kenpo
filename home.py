import streamlit as st
import pandas as pd
import json

with open('setting.json', 'r', encoding="UTF-8") as json_open:
    SETTING = json.load(json_open,)
with open('articles.json','r', encoding="UTF-8") as article_open:
    ARTICLE = json.load(article_open)

st.title(SETTING['title'])
st.header(SETTING['header'])
st.subheader(SETTING['subheader'])
st.caption(SETTING['caption'])

col0 , col1 = st.columns([2,1])
with col0:
    name = st.selectbox("名称",SETTING['names'])
with col1:
    select_options = ['前文'] + list(range(1,ARTICLE[name]['number']+1))
    article_number = str(st.selectbox("第n条",select_options))

if article_number in ARTICLE[name]:
    article_text = ARTICLE[name][article_number]['text']
    default_tags = ARTICLE[name][article_number]['tags']
else:
    article_text = ""
    default_tags = []

article = {}
# st.write(str(ARTICLE[name][article_number]['tags']))
with st.form("条文の入力",clear_on_submit=True):
    article['text'] = st.text_area("",value=article_text,placeholder="条文を書きます",height=500)
    col2, col3 = st.columns([2,0.3])
    with col2:
        article['tags']  = st.multiselect("タグ",SETTING['tags'], default=default_tags)
    with col3:
        st.write("")
        st.write("")
        submit_bool = st.form_submit_button("書込")
    if submit_bool:
        ARTICLE[name][article_number] = article
        with open('articles.json','w', encoding="UTF-8") as article_open:
            json.dump(ARTICLE, article_open, indent=4,ensure_ascii=False)
        submit_bool = False
        st.info('条文の書き込みを行いました')

    name=""
    article_number = 0
    article_text = ""
    default_tags = []
