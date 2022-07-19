import string
import streamlit as st
import json
import datetime
import os

with open('articles.json','r', encoding="UTF-8") as article_open:
    ARTICLE = json.load(article_open)

with open("template.py","r",encoding="UTF-8") as template_open:
    page_template = template_open.read()
    template = string.Template(page_template)
os.chdir("pages")

# with open('comment.json', 'r', encoding="UTF-8") as comment_open:
#     COMMENT = json.load(comment_open)

def create_a_page(name, article_number):
    with open(f"{name}-{article_number}.py","w",encoding="UTF-8") as f:
        py_body = template.safe_substitute({"name":name,"article_number":article_number})
        f.write(py_body)

name="日本国憲法"
# article_number = "前文"

for i in ['前文'] + list(range(1,ARTICLE[name]['number']+1)):
    create_a_page(name, i)