import streamlit as st
import articles_crud as artcrud
import user_crud as ucrud

st.markdown('# Editar articulos')
option = st.radio('Opciones',
                  ['Editar Articulo','Eliminar Articulo'])

if option == 'Eliminar Articulo':
    disable = True
else:
    disable = False

user = st.text_input('Ingresa tu usuario')
password = st.text_input('Ingresa tu contraseña')
titulo_articulo = st.text_input('Titulo del articulo')
new_titulo = st.text_input('Nuevo titulo del articulo',disabled=disable)
texto_articulo = st.text_input('Nuevo texto del articulo',disabled=disable)
tags_articulo = st.text_input('Tags del articulo',disabled=disable)
categories_articulo = st.text_input('Tags del articulo',disable=disable)

boton_opcion = st.button(option)

if not boton_opcion:
    st.stop()

if option == 'Eliminar Articulo' and ucrud.login(user,password):
    try:
        st.success(artcrud.delete_article(user,titulo_articulo))
    except:
        pass
elif option == 'Editar Articulo' and ucrud.login(user,password):
    pass
        
else:
    st.error('Usuario o contraseña incorrectos')