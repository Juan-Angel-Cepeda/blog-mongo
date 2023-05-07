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
    
st.title("Bienvendio al Blog")
st.markdown("## Por Juan Angel Cepeda Fernandez")
st.markdown("### Para Bases de Datos Avanzadas")
st.markdown("""# Guía para usar el blog
## Registrarse
1. Dirígete a la pestaña **Usuarios**.
2. Ingresa tu nombre de usuario y contraseña.
## Publicar un artículo

1. Ve a la pestaña **Publicar un artículo**.
2. Ingresa el título de tu artículo, el texto, los tags y las categorías.
3. Valida tu usuario y contraseña en los campos de validar usuario y contraseña.
4. Da clic en el botón **Crear** para publicarlo.

## Editar o eliminar artículos

1. Ve a la pestaña **Editar artículos**.
2. Selecciona si quieres editarlo o eliminarlo.
3. Ingresa tu usuario y contraseña. _Solo puedes eliminar o editar artículos que hayas publicado tú mismo_.
4. Ingresa el título de tu artículo.
    - Si deseas cambiar el título, ingresa un nuevo título en el campo correspondiente.
    - Si no deseas hacer cambios en el texto, tags o categorías, deja los espacios en blanco.
5. Pulsa el botón **Editar** o **Eliminar** según sea el caso.

## Ver artículos

- Para ver todos los artículos, dirígete a la sección **Artículos**.

## Buscar artículos

1. Dirígete a la sección **Buscar artículos**.
2. Puedes buscar por usuario, tag o categoría.

## Añadir comentario

1. Dirígete a la sección **Añadir comentario**.
2. Ingresa el título del artículo que deseas comentar.
3. Escribe tu comentario.
4. Ingresa tu usuario y contraseña. _Ten cuidado, los comentarios no se pueden borrar_.

_Nota: Las pestañas se encuentran en un sidebar._""")
