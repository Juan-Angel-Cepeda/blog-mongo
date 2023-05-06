import pymongo as mongo
from datetime import datetime

def create_article(title,text,user):
    conection = mongo.MongoClient("mongodb://localhost:27017")
    blog_conection = conection.blog
    users = blog_conection.users
    response = users.find_one({'user':user})
    now = datetime.now()
    date = now.date()
    date = str(date)
    new_article = {
        'title': title,
        'date': date,
        'text': text
    }

    if 'articles' in response:
        response['articles'].append(new_article)
    else:
        response['articles'] = [new_article]
    users.update_one({'user': user}, {'$set': response})
    return


def delete_article(title, user):
    
    connection = mongo.MongoClient("mongodb://localhost:27017")
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
            return 1
        else:
            print("Artículo no encontrado.")
            return 0
    else:
        print("El usuario no tiene artículos.")
        return 0


def get_all_articles():
    
    connection = mongo.MongoClient("mongodb://localhost:27017")
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
                
    return all_articles
    

def get_all_articles_from_a_user(user):
    connection = mongo.MongoClient("mongodb://localhost:27017")
    blog_connection = connection.blog
    users = blog_connection.users
    response = users.find({'user': user})
    articles = []
    for doc in response:
        articles.append(doc)

    """
    for document in response:
        if 'articles' in document:
            if len(document['articles']) > 0:
                for article in document['articles']:
                    article["username"] = user  # Agrega el nombre de usuario al artículo
                    articles.append(article)
    """
    return articles

get_all_articles_from_a_user('angel')
    
    
    