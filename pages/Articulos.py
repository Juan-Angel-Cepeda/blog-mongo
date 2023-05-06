import streamlit as st
import articles_crud as artcrud

st.title('Articles')
number_of_articles = len(artcrud.get_all_articles())
containers = []

for _ in range(number_of_articles):
    container = st.container()
    containers.append(container)

all_articles = artcrud.get_all_articles()

for i, article in enumerate(all_articles):
    with containers[i]:
        st.divider()
        st.markdown(f'## {article["title"]}')
        st.markdown(f'### {article["text"]}')
        st.markdown(f"**Autor:** {article['username']}")
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
        
        st.markdown("---")
