import streamlit as st
import json
import datetime

with open('articles.json','r', encoding="UTF-8") as article_open:
    ARTICLE = json.load(article_open)

name = "日本国憲法"
article_number = "103"
with open('comment.json', 'r', encoding="UTF-8") as comment_open:
    COMMENT = json.load(comment_open)

text = ARTICLE[name][article_number]['text']
if article_number=="前文":
    st.title(article_number)
else:
    st.title(f"第{article_number}条")
st.markdown(f'{text}')

with st.form("コメント",clear_on_submit=True):
    timestamp = datetime.datetime.now()
    timestamp_str = timestamp.strftime('%Y/%m/%d %H:%M:%S')
    user_name = st.text_input("名前")
    comment = st.text_area("コメント")
    form_data = {
            "timestamp":timestamp_str,
            "user":user_name,
            "comment":comment,
        }
    if not ("comment_data" in COMMENT[name][article_number]):
        COMMENT[name][article_number]["comment_data"]=[]
    COMMENT[name][article_number]["comment_data"].append(form_data)
    submit_bool =st.form_submit_button("送信")
    if submit_bool:
        with open('comment.json','w', encoding="UTF-8") as comment_write:
            json.dump(COMMENT, comment_write, indent=4,ensure_ascii=False)

for row in COMMENT[name][article_number]["comment_data"]:
    timestamp = row["timestamp"]
    user = row["user"]
    st.write(f"{timestamp}-{user}")
    st.write(row["comment"])