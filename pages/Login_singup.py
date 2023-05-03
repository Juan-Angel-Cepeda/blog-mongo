import streamlit as st
import user_crud as uscrud

st.title("Log-In or Sing-Up")
st.divider()

log_in,sing_up = st.tabs(["Log-in","Sing-Up"])
with log_in:
    user_li = st.text_input('User',key=1)
    password_li = st.text_input('Password',key=2)
    log_in = st.button("Log In")

with sing_up:
    user_sp = st.text_input('User',key=3)
    password_sp = st.text_input('Password',key=4)
    sing_up = st.button("Sing Up")
    

if log_in:
    response = uscrud.login(user_li,password_li)
    try:
        st.success(response)
    except:
        st.error(response)

if sing_up:
    try:
        uscrud.create_user(user_sp,password_sp)
        st.success("User created")
    except:
        st.error("User not created")
    
    
