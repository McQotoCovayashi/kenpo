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

# with open('comment.json', 'r', encoding="UTF-8") as comment_open:
#     COMMENT = json.load(comment_open)

def create_a_page(name, article_number):
    with open(f"{name}-{str(article_number).zfill(3)}.py","w",encoding="UTF-8") as f:
        py_body = template.safe_substitute({"name":name,"article_number":article_number})
        f.write(py_body)

name="日本国憲法"
# article_number = "前文"

COMMENT = {
    name:{str(i):{"comment_data":[]} for i in range(ARTICLE[name]['number']+1)}
}

os.chdir("pages")
for i in range(ARTICLE[name]['number']+1):
    create_a_page(name, i)

os.chdir("..")
with open("comment.json","w", encoding="UTF-8") as comment_write:
    json.dump(COMMENT, comment_write,indent=4,ensure_ascii=False)