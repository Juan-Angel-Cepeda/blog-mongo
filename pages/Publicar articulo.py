import streamlit as st
import user_crud as ucrud
import articles_crud as artcrud

st.title('Crea tu articulo')
st.markdown('### Cada artículo se relacionara con un usuario')
st.markdown('#### Para crear un articulo deberas ingresar usuario y contraseña')

title = st.text_input('Ingresa el titulo del articulo')
text = st.text_input('Intresa el texto de tu articulo')
user = st.text_input('Usuario')
password = st.text_input('Contraseña')

crear_articulo = st.button('Crear')
if not crear_articulo:
    st.stop()

if crear_articulo and ucrud.login(user,password):
    try:
        artcrud.create_article(title,text,user)
        st.success('Articulo creado')
    except:
        st.error('Articulo no creado')

else:
    st.error('Usuario o contraseña incorrectos')
    









