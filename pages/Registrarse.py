import streamlit as st
import user_crud as uscrud

st.title("Registrarse")
st.divider()

user_sp = st.text_input('Usuario')
password_sp = st.text_input('Contraseña')
sing_up = st.button("Registrarse")
if sing_up:
    try:
        uscrud.create_user(user_sp,password_sp)
        st.success("Usuario Creado")
    except:
        st.error("Error al crear usuario")
    
    
