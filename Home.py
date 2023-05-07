import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Blog mongo",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

fing = Image.open('./images/ingenieria.png')
uach = Image.open('./images/uach.png')

col1, col2, col3 = st.columns(3)    

with col1:
    st.image(fing,width=100)
with col3:
    st.image(uach,width=100)
    
st.title("Admin de Blog Mongo DB")
st.markdown("## 338832 Juan Angel Cepeda Fernandez")
st.markdown("### Bases de Datos Avanzadas")
st.markdown("#### Ve a la pagina Registrarse para registrar tu usuario")