import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import StringIO

# Título de la app
st.title("Generador de Nube de Palabras")
st.write("Autor: Jesus Alvarado-Huayhuaz")

# Subir archivo de texto
uploaded_file = st.file_uploader("Sube un archivo de texto", type="txt")

if uploaded_file is not None:
    # Leer el archivo
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    text = stringio.read()
    
    # Mostrar el texto cargado (opcional)
    st.subheader("Texto cargado:")
    st.write(text[:500])  # Muestra los primeros 500 caracteres

    # Generar la nube de palabras
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    # Mostrar la nube de palabras
    st.subheader("Nube de Palabras Generada")
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt)
