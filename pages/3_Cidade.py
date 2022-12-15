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

st.set_page_config (page_title='Visão Cidade', layout='wide')

# Leitura do arquivo 7527 rows × 21 columns
df = pd.read_csv('dataset/zomato.csv')

# Criando copia dos dados
df1 = df.copy()
# arquivo1.dtypes

# =======================================
# Barra Lateral
# =======================================
image_path = 'logo.png'
image = Image.open( image_path )
st.sidebar.image( image, width=80 )

st.sidebar.markdown( '# Fome Zero' )
st.sidebar.markdown( '## Filtros' )

traffic_options = st.sidebar.multiselect( 
    'Escolha os Paises que Deseja visualizar os Restaurantes',
    ['Brazil','England','Qatar','South Africa','Canada','Australia','Philippines','United States of America',
     'Singapure','United Arab Emirates','India','Indonesia','New Zeland','Sri Lanka','Turkey'], 
    default=['Brazil','England','Qatar','South Africa','Canada','Australia'] )

st.sidebar.markdown( """---""" )

st.sidebar.markdown( '### Dados Tratados' )

# Filtro de transito
linhas_selecionadas = df1['pais'].isin( traffic_options )
df1 = df1.loc[linhas_selecionadas, :]


# =======================================
# Layout no Streamlit
# =======================================
st.title( 'Visão Cidades' )
with st.container():
    st.markdown( '#### Top 10 cidades com mais restaurantes' )
    df_aux = df1.loc[:,['restaurant_id','city']].groupby(['city']).count()
    df_aux = df_aux.sort_values('restaurant_id',ascending=False).reset_index().head(10)
    fig = px.bar(df_aux,x='city',y='restaurant_id')
    st.plotly_chart(fig)
    
with st.container():
    col1,col2 = st.columns( 2, gap='large' )
    with col1:
        st.markdown( '##### Top 7 cidades com restaurantes com média de avaliação acima de 4' )
        df_aux1 = df1.loc[df1['aggregate_rating']>4,:]
        df_aux1 = df_aux1.loc[:,['restaurant_id','city']].groupby(['city']).count()
        df_aux1 = df_aux1.sort_values('restaurant_id',ascending=False).reset_index().head(7)
        fig = px.bar(df_aux1,x='city',y='restaurant_id')
        st.plotly_chart(fig)
        
    with col2:
        st.markdown('##### Top 7 cidades com restaurantes com média de avaliação abaixo de 2.5')
        df_aux1 = df1.loc[df1['aggregate_rating']<2.5,:]
        df_aux1 = df_aux1.loc[:,['restaurant_id','city']].groupby(['city']).count()
        df_aux1 = df_aux1.sort_values('restaurant_id',ascending=False).reset_index().head(7)
        fig = px.bar(df_aux1,x='city',y='restaurant_id')
        st.plotly_chart(fig)

with st.container():
        st.markdown( '#### Top 10 cidades com mais restaurantes com tipos culinários distintos' )
        df_aux = df1.loc[:,['cuisines','city']].groupby(['city']).nunique()
        df_aux = df_aux.sort_values('cuisines',ascending=False).reset_index().head(10)
        fig = px.bar(df_aux1,x='city',y='restaurant_id')
        st.plotly_chart(fig)