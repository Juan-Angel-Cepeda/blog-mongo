import streamlit as st
import user_crud as uscrud

st.title("Sing-Up")
st.divider()

user_sp = st.text_input('User',key=3)
password_sp = st.text_input('Password',key=4)
sing_up = st.button("Sing Up")
if sing_up:
    try:
        uscrud.create_user(user_sp,password_sp)
        st.success("User created")
    except:
        st.error("User not created")
    
    
