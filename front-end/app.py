import streamlit as st
import requests 

#URL da API fastAPI
API_URL = "http://127.0.0.1:8000"


#Roda o streamlit 
# python -m streamlit run app.py
st.set_page_config(page_title="gerenciador de Filmes", page_icon="")

#menu lateral
menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar filme"])

if menu == "Catalogo":
    st.subheader("todos os disponiveis")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            for filme in filmes:
                st.write(f"**{filme["titulo"]}**")
    else:
        st.error("erro ao acessar a API")
