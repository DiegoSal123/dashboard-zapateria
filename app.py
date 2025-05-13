import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
st.header('Demanda Potencial por País')
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='País', y='Demanda Hombre', data=demanda_df, ax=ax, color='skyblue')
sns.barplot(x='País', y='Demanda Mujer', data=demanda_df, ax=ax, color='salmon', alpha=0.7)
ax.set_title('Demanda Potencial de Calzado por Género')
ax.legend(['Demanda Hombre', 'Demanda Mujer'])
st.pyplot(fig)

# Sección de barreras de entrada
st.header('Barreras de Entrada por País')
st.dataframe(barreras_df)

# Sección de riesgo país
st.header('Intensidad de Riesgo País para Operaciones')
st.dataframe(riesgo_df)

# Sección de ventas de competidores
st.header('Ventas de Competidores por País')
fig2, ax2 = plt.subplots(figsize=(12, 6))
barras = ventas_df.set_index('País').plot(kind='bar', ax=ax2, colormap='Paired')
ax2.set_title('Ventas de Competidores por País')
st.pyplot(fig2)

st.write('Desarrollado para análisis de internacionalización de operaciones en Centroamérica.')

