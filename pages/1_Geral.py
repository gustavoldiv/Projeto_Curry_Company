#Libraries
from haversine  import haversine
import plotly.express as px
import plotly.graph_objects as go

# Bibliotecas necessárias
import pandas as pd
import streamlit as st
try:
    from PIL import Image
except ImportError:
    import Image
import folium
from streamlit_folium import folium_static

st.set_page_config (page_title='Visão Geral', layout='wide', page_icon="📊")

# Leitura do arquivo 7527 rows × 21 columns
df = pd.read_csv('dataset/zomato.csv')

# Criando copia dos dados
df1 = df.copy()
# arquivo1.dtypes

def convert_df(df):
    return df.to_csv().encode('utf-8')
csv = convert_df(df)

# =======================================
# Barra Lateral
# =======================================
image_path = 'logo.png'
image = Image.open( image_path )
st.sidebar.image( image, width=120 )
st.sidebar.markdown( '## Filtros' )

traffic_options = st.sidebar.multiselect( 
    'Escolha os Paises que Deseja visualizar os Restaurantes',
    ['Brazil','England','Qatar','South Africa','Canada','Australia','Philippines','United States of America',
     'Singapure','United Arab Emirates','India','Indonesia','New Zeland','Sri Lanka','Turkey'], 
    default=['Brazil','England','Qatar','South Africa','Canada','Australia'] )

st.sidebar.markdown( """---""" )
st.sidebar.markdown( '### Dados Tratados' )
st.sidebar.download_button( label="Download",data=csv,file_name='zomato.csv',mime='text/csv',)
st.sidebar.markdown( """---""" )


# Filtro de pais
linhas_selecionadas = df1['pais'].isin( traffic_options )
df1 = df1.loc[linhas_selecionadas, :]


# =======================================
# Layout no Streamlit
# =======================================
st.title( 'Fome Zero!' )
st.markdown('## O Melhor lugar para encontrar seu mais novo restaurante favorito!')

with st.container():
    st.markdown( '### Temos as seguintes marcas dentro da nossa plataforma:' )
    col1, col2, col3, col4,col5 = st.columns( 5, gap='large' )
    with col1:
        # Restaurantes únicos estão registrados
        df3= len(df1.loc[:,['restaurant_id']].groupby(['restaurant_id']).nunique().reset_index())
        col1.metric('Restaurantes',df3)

    with col2:
        # países únicos estão registrados
        df3 = len(df1.loc[:,['pais']].groupby(['pais']).nunique().reset_index())
        col2.metric('Países',df3)

    with col3:
        # Cidades
        df3= len(df1.loc[:,['city']].groupby(['city']).nunique().reset_index())
        col3.metric('Cidades',df3)  

    with col4:
        # Avaliações
        df_aux = df1.loc[df1['aggregate_rating']!=0,:]
        df3 = df_aux.shape[0]
        col4.metric('Avaliações',df3)

    with col5:
        # Tipos de Culinária
        df3= len(df1.loc[:,['cuisines']].groupby(['cuisines']).nunique().reset_index())
        col5.metric('Tipos de Culinária',df3)