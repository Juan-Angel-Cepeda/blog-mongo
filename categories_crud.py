from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st

uri = st.secrets["DB_MONGO_URI"]

def find_articles_by_categories(category):
    connection = MongoClient(uri, server_api=ServerApi('1'))
    blog_connection = connection.blog
    users = blog_connection.users
    all_users = users.find()

    articles_with_category = []
    for user in all_users:
        username = user.get("user")
        articles = user.get("articles", [])
        for article in articles:
            if category in article.get("categories", []):
                article["username"] = username
                articles_with_category.append(article)

    return articles_with_category