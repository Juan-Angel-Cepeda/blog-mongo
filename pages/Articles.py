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
        st.markdown(f"**Autor:** {article['username']}")
        st.markdown(f"**Fecha:** {article['date']}")
        st.subheader(article["title"])
        st.text(article["text"])
    


#containers = st.container(number_of_containers)