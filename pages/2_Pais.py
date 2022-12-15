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

st.set_page_config (page_title='Visão País', layout='wide')

# Leitura do arquivo 7527 rows × 21 columns
df = pd.read_csv('dataset/zomato.csv')

# Criando copia dos dados
df1 = df.copy()
# arquivo1.dtypes

# =======================================
# Barra Lateral
# =======================================
traffic_options = st.sidebar.multiselect( 
    'Escolha os Paises que Deseja visualizar os Restaurantes',
    ['Brazil','England','Qatar','South Africa','Canada','Australia','Philippines','United States of America',
     'Singapure','United Arab Emirates','India','Indonesia','New Zeland','Sri Lanka','Turkey'], 
    default=['Brazil','England','Qatar','South Africa','Canada','Australia'] )

st.sidebar.markdown( """---""" )

# Filtro de transito
linhas_selecionadas = df1['pais'].isin( traffic_options )
df1 = df1.loc[linhas_selecionadas, :]


# =======================================
# Layout no Streamlit
# =======================================
st.title( 'Visão Países' )
with st.container():
    st.markdown( '#### Qtde de Restaurantes por País' )
    df_aux = df1.loc[:,['restaurant_id','pais']].groupby(['pais']).count()
    df_aux = df_aux.sort_values('restaurant_id',ascending=False).reset_index()
    fig = px.bar(df_aux,x='pais',y='restaurant_id')
    st.plotly_chart(fig)
    
with st.container():
    st.markdown( '#### Qtde de Cidades por País' )
    df_aux = df1.loc[:,['city','pais']].groupby(['pais']).nunique()
    df_aux = df_aux.sort_values('city',ascending=False).reset_index()
    fig = px.bar(df_aux,x='pais',y='city')
    st.plotly_chart(fig)
    
with st.container():
    col1,col2 = st.columns( 2, gap='large' )
    with col1:
        st.markdown( '#### Média de avaliações feitas por país' )
        df_aux = df1.loc[:,['aggregate_rating','pais']].groupby(['pais']).mean()
        df_aux = df_aux.sort_values('aggregate_rating',ascending=False).reset_index()
        fig = px.bar(df_aux,x='pais',y='aggregate_rating')
        st.plotly_chart(fig)
        
    with col2:
        st.markdown( '#### Média de um prato para 2 pessoas por país' )
        df_aux = df1.loc[:,['average_cost_for_two','pais']].groupby(['pais']).mean()
        df_aux = df_aux.sort_values('average_cost_for_two',ascending=False).reset_index()
        fig = px.bar(df_aux,x='pais',y='average_cost_for_two')
        st.plotly_chart(fig)
