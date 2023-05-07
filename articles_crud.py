from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st

uri = st.secrets["DB_MONGO_URI"]

def create_article(title,text,user,tags,categories):
    conection = MongoClient(uri, server_api=ServerApi('1'))
    blog_conection = conection.blog
    users = blog_conection.users
    response = users.find_one({'user':user})
    now = datetime.now()
    date = now.date()
    date = str(date)
    tags_list = tags.split(',')
    categories_list = categories.split(',')
    
    new_article = {
        'title': title,
        'date': date,
        'text': text,
        'categories':categories_list,
        'comments':[],
        'tags':tags_list
    }

    if 'articles' in response:
        response['articles'].append(new_article)
    else:
        response['articles'] = [new_article]
    users.update_one({'user': user}, {'$set': response})
    conection.close()
    return

def delete_article(title, user):
    
    connection = MongoClient(uri, server_api=ServerApi('1'))
    blog_connection = connection.blog
    users = blog_connection.users
    response = users.find_one({'user': user})

    if 'articles' in response:
        article_index = None
        for index, article in enumerate(response['articles']):
            if article['title'] == title:
                article_index = index
                break

        if article_index is not None:
            response['articles'].pop(article_index)
            users.update_one({'user': user}, {'$set': response})
            connection.close()
            return "Articulo eliminado"
        else:
            connection.close()
            return "Articulo no encontrado"
    else:
        connection.close()
        return "El usuario no tiene articulos"

def get_all_articles():
    
    connection = MongoClient(uri, server_api=ServerApi('1'))
    blog_connection = connection.blog
    users = blog_connection.users
    all_users = users.find()
    
    all_articles = []
    for user in all_users:
        username = user.get("user")
        articles = user.get("articles",[])
        for article in articles:
            if article:
                article["username"] = username
                all_articles.append(article)
    
    connection.close()
    return all_articles    

def get_all_articles_from_a_user(user):
    connection = MongoClient(uri, server_api=ServerApi('1'))
    blog_connection = connection.blog
    users = blog_connection.users
    response = users.find({'user': user})
    articles = []
    for doc in response:
        articles.append(doc)
    
    connection.close()
    return articles

def delete_article(user,title):
    conection = MongoClient(uri, server_api=ServerApi('1'))
    blog_conection = conection.blog
    users = blog_conection.users
    response = users.find_one({'user':user})
    articles = response["articles"]

    article_index = -1
    for i, art in enumerate(articles):
        if art.get('title') == title:
            article_index = i
            break
        
    if article_index != -1:
        articles.pop(article_index)
        users.update_one({'user': user}, {'$set': {'articles': articles}})
        conection.close()
        return "Articulo eliminado"
    else:
        conection.close()
        return "Articulo no encontrado"
    
def editar_articulo(user,old_title,new_title,text,tags,categories):
    conection = MongoClient(uri, server_api=ServerApi('1'))
    blog_conection = conection.blog
    users = blog_conection.users
    response = users.find_one({'user': user})

    if 'articles' in response:
        articles = response['articles']
        for article in articles:
            if article.get('title') == old_title:
                if new_title != "":
                    article['title'] = new_title
                else:
                    article['title'] = article.get('title')
                if text != "":
                    article['text'] = text
                else:
                    article['text'] = article.get('text')
                if tags != "":
                    article['tags'] = tags.split(',')
                else:
                    article['tags'] = article.get('tags')
                if categories != "":
                    article['categories'] = categories.split(',')
                else:
                    article['categories'] = article.get('categories')
                break
        else:
            conection.close()
            return "No se encontro el articulo con ese titulo"
    else:
        conection.close()
        return f"El usuario {user} no tiene artículos."

    users.update_one({'user': user}, {'$set': response})
    conection.close()
    return "Articulo actualizado"
    