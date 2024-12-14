import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import StringIO
import string
from nltk.corpus import stopwords

# Cargar stopwords en español
stop_words = set(stopwords.words('spanish'))

# Función para limpiar puntuación y stopwords
def limpiar_puntuacion_stopwords(texto):
    puntuacion = []
    for s in string.punctuation:
        puntuacion.append(str(s))
    sp_puntuacion = ["¿", "¡", "“", "”", "…", ":", "–", "»", "«", "?", "!"]
    puntuacion += sp_puntuacion

    # Reemplazamos signos de puntuación por ""
    for p in puntuacion:
        texto = texto.lower().replace(p, "")

    # Reemplazamos stop_words por ""
    texto_lista = texto.split()
    texto_lista = [i.strip() for i in texto_lista]
    try:
        while stop in texto_lista:
            texto_lista.remove(stop)
    except:
        print("Error")
        pass

    texto_limpio = " ".join(texto_lista)

    return texto_limpio

# Título de la app
st.title("Generador de Nube de Palabras")

# Subir archivo de texto
uploaded_file = st.file_uploader("Sube un archivo de texto", type="txt")

# Opciones para seleccionar color de fondo
background_color = st.selectbox(
    "Selecciona el color de fondo", 
    ["white", "black", "blue", "yellow", "green", "red"]
)

if uploaded_file is not None:
    # Leer el archivo
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    text = stringio.read()

    # Limpiar el texto cargado
    text_limpio = limpiar_puntuacion_stopwords(text)
    
    # Generar la nube de palabras con el color de fondo seleccionado
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color=background_color
    ).generate(text_limpio)

    # Mostrar la nube de palabras
    st.subheader("Nube de Palabras Generada")
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt)
