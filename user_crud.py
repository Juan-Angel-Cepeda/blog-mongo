import pymongo as mongo

def create_user(name,password):
    conection = mongo.MongoClient("mongodb://localhost:27017")   
    blog_conection = conection.blog
    users = blog_conection.Users
    new_user = {
        'user':name,
        'password':password,
        'articles':[{}],
        'coments':[{}]
    }
    users.insert_one(new_user)
    conection.close()
    return

def login(name,password):
    conection = mongo.MongoClient("mongodb://localhost:27017")   
    blog_conection = conection.blog
    users = blog_conection.Users
    
    

def sing_up(name,email):
    conection = mongo.MongoClient("mongodb://localhost:27017")   
    blog_conection = conection.blog
    users = blog_conection.Users
    
