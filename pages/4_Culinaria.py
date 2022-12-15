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

st.set_page_config (page_title='Visão Culinária', layout='wide')

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
st.title( 'Visão Tipos de Cozinhas' )
st.markdown('## Melhores Restaurantes dos Principais tipos Culinários')
with st.container():
    col1, col2, col3, col4,col5 = st.columns( 5, gap='large' )
    with col1:
        df_aux = df1[df1['cuisines'].str.contains('Italian', na = False)]
        df_aux = df_aux.loc[df_aux['aggregate_rating']!=0]
        df_aux = df_aux.loc[:,['aggregate_rating','restaurant_name']].groupby(['restaurant_name']).mean()
        df_aux = df_aux.sort_values('aggregate_rating',ascending=False).reset_index()
        df3 = df_aux.loc[0,'restaurant_name']
        df4 = df_aux.loc[0,'aggregate_rating']
        col1.write('Italiana')
        col1.metric(df3,df4)
        
    with col2:
        df_aux = df1[df1['cuisines'].str.contains('American', na = False)]
        df_aux = df_aux.loc[df_aux['aggregate_rating']!=0]
        df_aux = df_aux.loc[:,['aggregate_rating','restaurant_name']].groupby(['restaurant_name']).mean()
        df_aux = df_aux.sort_values('aggregate_rating',ascending=False).reset_index()
        df3 = df_aux.loc[0,'restaurant_name']
        df4 = df_aux.loc[0,'aggregate_rating']
        col2.write('Americana')
        col2.metric(df3,df4)

    with col3:
        df_aux = df1[df1['cuisines'].str.contains('Japane', na = False)]
        df_aux = df_aux.loc[df_aux['aggregate_rating']!=0]
        df_aux = df_aux.loc[:,['aggregate_rating','restaurant_name']].groupby(['restaurant_name']).mean()
        df_aux = df_aux.sort_values('aggregate_rating',ascending=False).reset_index()
        df3 = df_aux.loc[0,'restaurant_name']
        df4 = df_aux.loc[0,'aggregate_rating']
        col3.write('Japonesa')
        col3.metric(df3,df4)
        
    with col4:
        df_aux = df1[df1['cuisines'].str.contains('Arabia', na = False)]
        df_aux = df_aux.loc[df_aux['aggregate_rating']!=0]
        df_aux = df_aux.loc[:,['aggregate_rating','restaurant_name']].groupby(['restaurant_name']).mean()
        df_aux = df_aux.sort_values('aggregate_rating',ascending=False).reset_index()
        df3 = df_aux.loc[0,'restaurant_name']
        df4 = df_aux.loc[0,'aggregate_rating']
        col4.write('Arabica')
        col4.metric(df3,df4)



with st.container():
    st.markdown( '#### Top 10 Restaurantes')
    df_aux1 = df1.loc[:,['restaurant_id','restaurant_name','pais','city','cuisines','average_cost_for_two','aggregate_rating','votes']]
    df_aux1 = df_aux1.sort_values('aggregate_rating',ascending=False).reset_index().head(10)
    st.dataframe(df_aux1)