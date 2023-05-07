import user_crud as ucrud
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = st.secrets["DB_MONGO_URI"]

def save_coment(comentario,articulo,user_comentando,password_usuario_comentado):
    connection = MongoClient(uri,server_api=ServerApi('1'))
    blog_connection = connection.blog
    users = blog_connection.users
    all_users = users.find()

    if ucrud.login(user_comentando, password_usuario_comentado):
        comentario_a_guardar = f"{user_comentando} dice:  {comentario}"
        article_found = False

        for user in all_users:
            for i, article in enumerate(user["articles"]):
                if article["title"] == articulo:
                    # Agrega el comentario al artículo
                    user["articles"][i]["comments"].append(comentario_a_guardar)
                    
                    # Actualiza el documento del usuario en la base de datos
                    users.update_one({'user': user["user"]}, {'$set': user})
                    article_found = True
                    break

            if article_found:
                break
        else:
            connection.close()
            return "No se encontró el artículo."
        connection.close()
        return "Comentario guardado."
    else:
        connection.close()
        return "Usuario o contraseñas incorrectas"
    
        
    
    