import pymongo as mongo

def create_article(title,date,text):
    conection = mongo.MongoClient("mongodb://localhost:27017")
    blog_conection = conection.blog
    users = blog_conection.Users
    
    new_article = {
        
    }
    
    