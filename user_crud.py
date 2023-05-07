from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st
import hashlib

uri = st.secrets["DB_MONGO_URI"]

def create_user(name,password):
    conection = MongoClient(uri, server_api=ServerApi('1'))
    blog_conection = conection.blog
    users = blog_conection.users
    hash_password = hashlib.sha256(password.encode()).hexdigest()
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
        hash_passworddb = response['password']
        conection.close()
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        if name == userdb and hash_password == hash_passworddb:
            return True
    except:
            return False
    
