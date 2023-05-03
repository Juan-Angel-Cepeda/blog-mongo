import streamlit as st

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
