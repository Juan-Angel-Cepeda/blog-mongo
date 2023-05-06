import streamlit as st
import articles_crud as artcrud

st.title(f'Articles por usuario')

user = st.text_input("Busca los articulos de un usuario")
buscar = st.button('Buscar articulos')

if buscar:
    number_of_articles = len(artcrud.get_all_articles_from_a_user(user))
    st.markdown(f'# Artiuclos publicados por {user}')
    containers = []
    
    for _ in range(number_of_articles):
        container = st.container()
        containers.append(container)

    all_articles = artcrud.get_all_articles_from_a_user(user)
    
    count = 0
    for user_document in all_articles:
        user_articles = user_document["articles"]
        
        for article in user_articles:
            
            if not article:  # Ignora los elementos vacíos en la lista de artículos
                continue

            with containers[count]:
                st.divider()
                st.markdown(f'## {article["title"]}')
                st.markdown(f'{article["text"]}')
                st.markdown(f"**Fecha:** {article['date']}")
        
        count += 1