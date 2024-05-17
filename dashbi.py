import streamlit as st
import streamlit.components.v1 as components

# Título da aplicação
st.title('Dashboard Interativo do Power BI')

# Texto de introdução
st.write('Bem-vindo ao dashboard interativo!')

# URL de incorporação do Power BI
power_bi_url = 'https://app.powerbi.com/view?r=eyJrIjoiY2JlZWRlYmYtY2VkYy00OTI1LWJjODYtY2UwODhhMTAzZTJjIiwidCI6IjZkNDg1YWY3LTAxZjYtNGE2MC05OWEwLTQzOTQyNzJiMjUzNSJ9'

# Exibindo o relatório do Power BI de forma interativa
components.iframe(power_bi_url, width=1200, height=800, scrolling=True)
