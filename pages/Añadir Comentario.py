import streamlit as st
import comments_crud as commcrud

st.markdown('### Añadir comentarios')


titulo = st.text_input('Titulo del articulo a comentar')
comentario = st.text_input('Comenta aqui: ')
usuario_comentando = st.text_input('Ingresa tu usuario')
pass_usuario_comentando = st.text_input('Ingresa tu contraseña',type='password')
comentar = st.button('comentar')
if comentar:
    try:
        st.success(commcrud.save_coment(comentario,titulo,usuario_comentando,pass_usuario_comentando))
    except:
        st.error('Comentario  no guardado')
        
    