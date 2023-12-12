import streamlit as st
from helpers import adapt_content_for_kids
from translate import Translator
import base64



# Set the page config as the first command
st.set_page_config(page_title="WikiExplorer", page_icon="🌐", layout="wide")

# Función para obtener la representación en base64 de una imagen
def get_image_base64(path):
    # Determine the image format based on the file extension
    file_extension = path.split('.')[-1].lower()
    if file_extension == 'svg':
        # For SVG images
        with open(path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
        return f"data:image/svg+xml;base64,{encoded}"
    elif file_extension == 'png':
        # For PNG images
        with open(path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
        return f"data:image/png;base64,{encoded}"
    else:
        raise ValueError("Unsupported image format. Supported formats: SVG and PNG")


def main():
    # Use columns to center the header
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
 
        st.markdown(f"<div style='text-align: center;'><h3>🌐 WikiExplorers:\n Aventuras del Saber / Knowledge Adventures 🌟</h3></div>", unsafe_allow_html=True)
    
        # Center the robot image using HTML and CSS
        robot_img_base64 = get_image_base64("./assets/robot_image.png")
        st.markdown(f"<div style='text-align: center;'><img src='{robot_img_base64}' width='600' style='margin: 0 auto;'></div>", unsafe_allow_html=True)

    

    # Use columns to center the text input
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        query = st.text_input("¿Sobre qué te gustaría aprender hoy? / What would you like to learn about today?")
 
    if query:
        col1, col2, col3 = st.columns([1, 2, 1])
        with st.spinner(f"Generando boletín para / Generating newsletter for {query}"):
            adapted_content = adapt_content_for_kids(query)

            # Traducir el contenido en inglés al español
            translator = Translator(to_lang="es")
            adapted_content_es_translated = translator.translate(adapted_content)

            # Use columns to center the story content
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.write("🇪🇸 Aquí tienes tu historia en español:")
                st.write(adapted_content_es_translated)

                st.write("🇺🇸 Here's Your Fun Story in English:")
                st.write(adapted_content)
if __name__ == '__main__':
    main()
    
    



# Obtén la representación en base64 de tus imágenes
github_icon_base64 = get_image_base64("./assets/github.svg")
linkedin_icon_base64 = get_image_base64("./assets/linkedin.svg")

# URLs de tus perfiles
github_url = "https://github.com/limbpuma"
linkedin_url = "https://www.linkedin.com/in/limber-martinez-developer/"

# Usar st.markdown para agregar enlaces con imágenes codificadas en base64
st.markdown(f"""
    <div style="text-align: center; display: flex; justify-content: center; align-items: center; gap: 20px;">
        <a href="{github_url}" target="_blank">
            <img src="{github_icon_base64}" alt="GitHub" style="width: 20px; height: 20px;">
        </a>
        <a href="{linkedin_url}" target="_blank">
            <img src="{linkedin_icon_base64}" alt="LinkedIn" style="width: 20px; height: 20px;">
        </a>
    </div>
""", unsafe_allow_html=True)
# Mensaje "Hecho con Python, Langchain y Streamlit"
st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <p>Made with ❤️ en Python, Langchain y Streamlit</p>
    </div>
""", unsafe_allow_html=True)    
    