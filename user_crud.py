from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st

uri = st.secrets["DB_MONGO_URI"]

def create_user(name,password):
    conection = MongoClient(uri, server_api=ServerApi('1'))
    blog_conection = conection.blog
    users = blog_conection.users
    new_user = {
        'user':name,
        'password':password,
        'articles':[]
    }
    users.insert_one(new_user)
    conection.close()
    return

def login(name,password):
    conection = MongoClient(uri, server_api=ServerApi('1'))
    blog_conection = conection.blog
    users = blog_conection.users
    try:
        response = users.find_one({'user':name})
        userdb = response['user']
        passworddb = response['password']
        conection.close()
        if name == userdb and password == passworddb:
            return True
    except:
            return False
    
