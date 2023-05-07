import streamlit as st
import user_crud as uscrud

st.title("Usuarios")
st.divider()
containerSing,containerDel = st.container(2)

with containerSing:
    st.subheader('Crea tu usuario')
    user_sp = st.text_input('Usuario')
    password_sp = st.text_input('Contraseña',type='password')
    sing_up = st.button("Registrarse")
    if sing_up:
        try:
            uscrud.create_user(user_sp,password_sp)
            st.success("Usuario Creado")
        except:
            st.error("Error al crear usuario")
with containerDel:
    st.subheader('Elimina tu usuario')
    user_del = st.text_input('Nombre de usuario')
    password_del = st.text_input('Contraseña',type='password')
    del_button = st.button('Eliminame')
    if del_button:
        try:
            st.succes(uscrud.delete_user(user_del,password_del))
        except:
            st.error('Error')
            
            
    
