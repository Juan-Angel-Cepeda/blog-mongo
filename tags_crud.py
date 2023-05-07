import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = st.secrets["DB_MONGO_URI"]

def find_articles_by_tag(tag):
    connection = MongoClient(uri,server_api=ServerApi('1'))
    blog_connection = connection.blog
    users = blog_connection.users
    all_users = users.find()

    articles_with_tag = []
    for user in all_users:
        username = user.get("user")
        articles = user.get("articles", [])
        for article in articles:
            if tag in article.get("tags", []):
                article["username"] = username
                articles_with_tag.append(article)

    connection.close()
    return articles_with_tag