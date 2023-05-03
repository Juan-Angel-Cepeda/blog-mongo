import streamlit as st

st.title('Publish your article')
st.markdown('### Cada artículo se relacionara con un usuario')
user = st.text_input("Ingresa tu usuario")


create_article = st.button("Create")