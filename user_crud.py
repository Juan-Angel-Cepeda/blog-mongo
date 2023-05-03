import pymongo as mongo

def create_user(name,email):
    conection = mongo.MongoClient("mongodb://localhost:27017")   
    blog_conection = conection.blog
    users = blog_conection.Users
    new_user = {
        'Name':name,
        'email':email,
        'articles':[{}],
        'coments':[{}]
    }
    users.insert_one(new_user)
    conection.close()
    pass

def login(name,email):
    pass
    

create_user("angel","jangelcepeda@protonmail.com")