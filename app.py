import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Configuración del título del dashboard
st.set_page_config(page_title='Dashboard de Internacionalización de Zapatos en Centroamérica', layout='wide')

# Cargar los datos desde los archivos CSV
@st.cache_data
def load_data():
    demanda_df = pd.read_csv('https://raw.githubusercontent.com/DiegoSal123/dashboard-zapateria/main/demanda_potencial.csv')
    barreras_df = pd.read_csv('https://raw.githubusercontent.com/DiegoSal123/dashboard-zapateria/main/barreras_por_pais.csv')
    riesgo_df = pd.read_csv('https://raw.githubusercontent.com/DiegoSal123/dashboard-zapateria/main/riesgo_pais.csv')
    ventas_df = pd.read_csv('https://raw.githubusercontent.com/DiegoSal123/dashboard-zapateria/main/ventas.csv')
    return demanda_df, barreras_df, riesgo_df, ventas_df

demanda_df, barreras_df, riesgo_df, ventas_df = load_data()

# Mostrar el título del dashboard
st.title('Dashboard Interactivo para la Internacionalización de Zapatos en Centroamérica')

# Sección de demanda potencial
st.header('📊 Demanda Potencial por País')
demanda_long = demanda_df.melt(id_vars=['País'], var_name='Género', value_name='Demanda')
demanda_fig = px.bar(demanda_long, x='País', y='Demanda', color='Género', barmode='group', title='Demanda Potencial de Calzado por Género', template='plotly_white', color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(demanda_fig)

# Sección de barreras de entrada
st.header('🛑 Barreras de Entrada por País')
st.dataframe(barreras_df.style.set_properties(**{'background-color': '#f9f9f9', 'border-color': 'black', 'color': 'black', 'border-width': '1px', 'font-size': '14px'}).set_table_styles([{'selector': 'th', 'props': [('background-color', '#1f77b4'), ('color', 'white'), ('font-weight', 'bold'), ('text-align', 'center')]}]))

# Sección de riesgo país
st.header('⚠️ Intensidad de Riesgo País para Operaciones')
st.dataframe(riesgo_df.style.set_properties(**{'background-color': '#f9f9f9', 'border-color': 'black', 'color': 'black', 'border-width': '1px', 'font-size': '14px'}).set_table_styles([{'selector': 'th', 'props': [('background-color', '#d62728'), ('color', 'white'), ('font-weight', 'bold'), ('text-align', 'center')]}]))

# Sección de ventas de competidores
st.header('🏆 Ventas de Competidores por País')
ventas_long = ventas_df.melt(id_vars=['País'], var_name='Competidor', value_name='Ventas')
ventas_fig = px.bar(ventas_long, x='País', y='Ventas', color='Competidor', barmode='group', title='Ventas de Competidores por País', template='plotly_white', color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(ventas_fig)

st.write('Desarrollado para análisis de internacionalización de operaciones en Centroamérica.')
