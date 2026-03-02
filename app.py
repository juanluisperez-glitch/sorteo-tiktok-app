import streamlit as st
import requests
import random

st.title("🎉 Sorteo Aleatorio de TikTok")
st.write("Ingresa el enlace de un video para elegir un comentario ganador al azar.")

url_tiktok = st.text_input("Enlace del video de TikTok:")

if st.button("Elegir Ganador"):
    if url_tiktok:
        st.info("Conectando con TikTok para buscar comentarios reales... 🕵️‍♂️")
        
        # 1. Leemos tu llave secreta de la bóveda de Streamlit
        try:
            api_key = st.secrets["RAPIDAPI_KEY"]
        except KeyError:
            st.error("Error: No se encontró la API Key en los Secrets de Streamlit.")
            st.stop()
        
        # 2. Configuramos la conexión a RapidAPI (Usando la API que encontraste)
        url_api = "https://tiktok-scraper7.p.rapidapi.com/comment/list"
        
        # Parámetros (le mandamos el link que el usuario pegó en la caja de texto)
        querystring = {"url": url_tiktok, "count": "50"} 
        
        headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "tiktok-scraper7.p.rapidapi.com"
        }
        
        try:
            # 3. Hacemos la llamada real a internet
            response = requests.get(url_api, headers=headers, params=querystring)
            datos = response.json() # Convertimos la respuesta a un diccionario de Python
            
            # 4. Extraemos la lista de comentarios de la respuesta
            # (Asumimos la estructura más común de esta API, si cambia, lo ajustaremos)
            comentarios_reales = datos.get("data", {}).get("comments", [])
            
            # Si la API tiene otra estructura, a veces vienen directos en 'data'
            if not comentarios_reales and isinstance(datos.get("data"), list):
                comentarios_reales = datos.get("data")
                
            if comentarios_reales:
                # 5. Elegimos uno al azar
                ganador = random.choice(comentarios_reales)
                
                # Extraemos el texto y el autor (Ajustando nombres comunes de variables)
                texto_comentario = ganador.get("text", "Comentario sin texto")
                
                # Buscamos el nombre de usuario en distintas posibles rutas
                usuario_info = ganador.get("user", {})
                nombre_usuario = usuario_info.get("unique_id", usuario_info.get("nickname", "Usuario_Desconocido"))
                
                # 6. ¡Mostramos al ganador!
                st.success("¡Tenemos un ganador real!")
                st.balloons()
                st.header(f"👑 @{nombre_usuario}")
                st.write(f"💬 Comentario: {texto_comentario}")
                
            else:
                st.warning("No se encontraron comentarios. Revisa que el video sea público y tenga comentarios.")
                # Mostramos los datos crudos para ver qué nos mandó la API y poder arreglarlo
                st.write("🔍 Diagnóstico: Esto es lo que respondió la API:")
                st.json(datos)
                
        except Exception as e:
            st.error(f"Hubo un error al conectar con la API: {e}")
    else:
        st.warning("Por favor, ingresa un enlace válido.")