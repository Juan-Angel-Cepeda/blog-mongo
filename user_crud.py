import pymongo as mongo

def create_user(name,password):
    conection = mongo.MongoClient("mongodb://localhost:27017")   
    blog_conection = conection.blog
    users = blog_conection.users
    new_user = {
        'user':name,
        'password':password,
        'articles':[{}],
        'coments':[]
    }
    users.insert_one(new_user)
    conection.close()
    return

def login(name,password):
    conection = mongo.MongoClient("mongodb://localhost:27017")   
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
    
