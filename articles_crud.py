import pymongo as mongo
from datetime import datetime

def create_article(title,text,user,tags,categories):
    conection = mongo.MongoClient("mongodb://localhost:27017")
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
    
    return articles

def delete_article(user,title):
    conection = mongo.MongoClient("mongodb://localhost:27017")
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
        return "Articulo eliminado"
    else:
        return "Articulo no encontrado"
    
def editar_articulo(user,old_title,new_title,text,tags,categories):
    conection = mongo.MongoClient("mongodb://localhost:27017")
    blog_conection = conection.blog
    users = blog_conection.users
    response = users.find_one({'user': user})

    if 'articles' in response:
        articles = response['articles']
        for article in articles:
            if article.get('title') == old_title:
                article['title'] = new_title
                article['text'] = text
                article['tags'] = tags.split(',')
                article['categories'] = categories.split(',')
                break
        else:
            print("No se encontró el artículo con el título especificado.")
    else:
        print(f"El usuario {user} no tiene artículos.")

    users.update_one({'user': user}, {'$set': response})
    return
    