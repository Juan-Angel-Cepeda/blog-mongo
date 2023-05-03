import pymongo as mongo

def create_article(title,date,text):
    conection = mongo.MongoClient("mongodb://localhost:27017")
    blog_conection = conection.blog
    users = blog_conection.Users
    
    new_article = {
        title:title,
        date:date,
        text:text
    }
    
    users.insert_one(new_article)
    
    