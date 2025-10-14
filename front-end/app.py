import streamlit as st
import requests 

#URL da API fastAPI
API_URL = "http://127.0.0.1:8000"


#Roda o streamlit 
# python -m streamlit run app.py
st.set_page_config(page_title="gerenciador de fclearilmes", page_icon="")

#menu lateral
menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar filme"])

if menu == "Catalogo":
    st.subheader("todos os filmes disponiveis")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            st.dataframe(filmes)
    else:
        st.error("erro ao acessar a API")

elif menu == "Adicionar filme":
    st.subheader("➕ Adicionar filmes")
    titulo = st.text_input("titulo do filme")
    genero = st.text_input("Gênero")
    ano = st.number_input("Ano de Lançamento", min_value=1880, max_value=2100, step=1)
    avaliacao = st.number_input("Avaliação de (0 a 10)", min_value=0.0, max_value=10.0, step=0.1 )
    if st.button("salvar filme"):
        dados = {"titulo": titulo, "genero":  genero, "ano": ano, "avaliacao": avaliacao}
        response = requests.post(f"{API_URL}/filmes", params=dados)
        if response.status_code == 200:
            st.success("filme adicionando com sucesso!")
        else:
            st.error("erro ao adicionar o filme")

