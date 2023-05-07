import streamlit as st
import articles_crud as artcrud
import tags_crud as tcrud
import categories_crud as catcrud

st.title(f'Busqueda de articulos')

tabUsuario, tabTag, tabCategoria = st.tabs(["Buscar por Usuario","Buscar por Tag","Buscar por Categoria"])


with tabUsuario:
    user = st.text_input("Busca los articulos de un usuario")
    buscar = st.button('Buscar articulos')
    if buscar:

        number_of_articles = len(artcrud.get_all_articles_from_a_user(user))
        st.markdown(f'# Articulos publicados por {user}')
        containers = []

        for _ in range(number_of_articles):
            container = st.container()
            containers.append(container)

        all_articles = artcrud.get_all_articles_from_a_user(user)

        count = 0
        for user_document in all_articles:
            user_articles = user_document["articles"]

            for article in user_articles:

                if not article:
                    continue

                with containers[count]:
                    st.divider()
                    st.markdown(f'## {article["title"]}')
                    st.markdown(f'{article["text"]}')
                    st.markdown(f"**Fecha:** {article['date']}")
                    st.markdown("##### Tags:")
                    tags_string = ", ".join(article['tags'])
                    st.markdown(tags_string)

                    st.markdown("##### Categorías:")
                    category_sring = ", ".join(article["categories"])
                    st.markdown(category_sring)

                    st.markdown("##### Comentarios:")
                    if len(article['comments']) > 0:
                        for comment in article['comments']:
                            st.markdown(f"- {comment}")
                    else:
                        st.markdown("No hay comentarios.")

            count += 1

with tabTag:
    
    tag = st.text_input('Buscar los artiuclos por tags')
    buscar = st.button('Buscar por tag')
    if buscar:
        number_of_articles = len(tcrud.find_articles_by_tag(tag))
        st.markdown(f'# Articulos con el Tag: {tag}')
        containers = []

        for _ in range(number_of_articles):
            container = st.container()
            containers.append(container)
        
        all_articles = tcrud.find_articles_by_tag(tag)
        
        count = 0

        for article in all_articles:

            if not article:
                continue
            with containers[count]:
                st.divider()
                st.markdown(f'## {article["title"]}')
                st.markdown(f'{article["text"]}')
                st.markdown(f"**Fecha:** {article['date']}")
                st.markdown("##### Tags:")
                tags_string = ", ".join(article['tags'])
                st.markdown(tags_string)
                st.markdown("##### Categorías:")
                category_sring = ", ".join(article["categories"])
                st.markdown(category_sring)
                st.markdown("##### Comentarios:")
                if len(article['comments']) > 0:
                    for comment in article['comments']:
                        st.markdown(f"- {comment}")
                else:
                    st.markdown("No hay comentarios.")
            count += 1

with tabCategoria:
    
    categoria = st.text_input('Buscar los articulos por categoria')
    buscar = st.button('Buscar por categoria')
    if buscar:
        number_of_articles = len(catcrud.find_articles_by_categories(categoria))
        st.markdown(f'# Articulos con la categoria: {categoria}')
        containers = []

        for _ in range(number_of_articles):
            container = st.container()
            containers.append(container)
        
        all_articles = catcrud.find_articles_by_categories(categoria)
        
        count = 0

        for article in all_articles:

            if not article:
                continue
            with containers[count]:
                st.divider()
                st.markdown(f'## {article["title"]}')
                st.markdown(f'{article["text"]}')
                st.markdown(f"**Fecha:** {article['date']}")
                st.markdown("##### Tags:")
                tags_string = ", ".join(article['tags'])
                st.markdown(tags_string)
                st.markdown("##### Categorías:")
                category_sring = ", ".join(article["categories"])
                st.markdown(category_sring)
                st.markdown("##### Comentarios:")
                if len(article['comments']) > 0:
                    for comment in article['comments']:
                        st.markdown(f"- {comment}")
                else:
                    st.markdown("No hay comentarios.")
            count += 1
    