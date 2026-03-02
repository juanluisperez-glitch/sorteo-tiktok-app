import streamlit as st
import requests
import random
import http.client

# Título de tu aplicación
st.title("🎉 Sorteo Aleatorio de TikTok")
st.write("Ingresa el enlace de un video para elegir un comentario ganador al azar.")

# Caja de texto para el link
url_tiktok = st.text_input("Enlace del video de TikTok:")

# Botón para accionar la búsqueda
if st.button("Elegir Ganador"):
    if url_tiktok:
        st.info("Buscando comentarios... (Esto puede tomar unos segundos)")
        
        # --- AQUÍ VA LA CONEXIÓN A RAPIDAPI ---
        # Nota: Deberás reemplazar 'TU_API_KEY' y la URL con los datos exactos que te dé RapidAPI
        url_api = http.client.HTTPSConnection("tiktok-scraper7.p.rapidapi.com")
        headers = {
            "X-RapidAPI-Key": "59026de524mshbd31ad74560b8d9p1aa7e5jsn63d6e7fbebff",
            "X-RapidAPI-Host": "tiktok-scraper7.p.rapidapi.com"
        }
        
        try:
            # Simulamos la respuesta para probar la interfaz visual primero
            # Una vez conectes la API, borrarás estos comentarios simulados y usarás 'requests.get()'
            comentarios = [
                {"usuario": "usuario_1", "texto": "¡Yo participo!"},
                {"usuario": "maria_dev", "texto": "Qué gran video."},
                {"usuario": "mac_user", "texto": "Quiero ganar el sorteo"}
            ]
            
            # Elegir ganador
            ganador = random.choice(comentarios)
            
            st.success("¡Tenemos un ganador!")
            st.balloons() # Animación de globos en la pantalla
            st.header(f"👑 @{ganador['usuario']}")
            st.write(f"💬 Comentario: {ganador['texto']}")
            
        except Exception as e:
            st.error(f"Hubo un error al obtener los comentarios: {e}")
    else:
        st.warning("Por favor, ingresa un enlace válido.")