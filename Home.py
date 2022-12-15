import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Página inicial",
    page_icon="", layout='wide')

st.markdown("""
    ### Como utilizar o Dashboard?
    - Visão Geral:
        - Dados gerais dos restaurantes
    - Visão País:
        - Qtde de Restaurantes por País
        - Qtde de Cidades por País
        - Média de avaliações feitas por país
        - Média de um prato para 2 pessoas por país
    - Visão Cidade:
        - Top 10 cidades com mais restaurantes
        - Top 7 cidades com restaurantes com média de avaliação acima de 4
        - Top 7 cidades com restaurantes com média de avaliação abaixo de 2.5
        - Top 10 cidades com mais restaurantes com tipos culinários distintos
    - Visão Culinária
        - Melhores Restaurantes dos Principais tipos Culinários
        - Top 10 Restaurantes por avaliação
    """)