import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

# Configurar a página para o layout 'wide'
st.set_page_config(layout="wide")

# Estilizar a barra lateral
st.markdown(
"""
<style>
.css-1lcbmhc.e1fqkh3o3 {
    background-color: #3e5265;
    color: #f2f2f2;
}
.css-1lcbmhc.e1fqkh3o3:hover {
    background-color: #3e5265;
    color: #bdcdd8;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("Dashboard")


# Exibir um exemplo da cor selecionada
st.markdown(
    f'<div style="background-color:s#f2f2f;padding:10px;border-radius:5px;"></div>',
    unsafe_allow_html=True
)

# Função para exibir cada relatório
def show_report(url):
    components.iframe(url, width=1200, height=750, scrolling=True)

# Lista de relatórios com título e URL
reports = {
    "Relatório 1": "https://app.powerbi.com/view?r=eyJrIjoiZWFiN2VlZjQtZmNkMS00YmJkLWI1MzItYjYxNDMyYjdiZjY1IiwidCI6IjZkNDg1YWY3LTAxZjYtNGE2MC05OWEwLTQzOTQyNzJiMjUzNSJ9",
    "Relatório 2": "https://app.powerbi.com/view?r=eyJrIjoiNWE0NjY3MjEtMTdkNi00YjAwLTg3ZjgtNmM1ZDhhMzY1MGU0IiwidCI6IjZkNDg1YWY3LTAxZjYtNGE2MC05OWEwLTQzOTQyNzJiMjUzNSJ9",
    "Relatório 3": "https://app.powerbi.com/view?r=eyJrIjoiNDhmZmRhNzMtYzBiMS00ZjRmLThiMGUtYjc3NzkyNGRlODIwIiwidCI6IjZkNDg1YWY3LTAxZjYtNGE2MC05OWEwLTQzOTQyNzJiMjUzNSJ9",
    "Relatório 4": "https://app.powerbi.com/view?r=eyJrIjoiMzBiMWI3MjQtYzQ0Zi00OWI0LTliY2ItNTAyNmQ4NzY3MzVkIiwidCI6IjZkNDg1YWY3LTAxZjYtNGE2MC05OWEwLTQzOTQyNzJiMjUzNSJ9",
    "Relatório 5": "https://app.powerbi.com/view?r=eyJrIjoiYmY3NWIyNGMtNDdlYy00Y2JkLWEzYzgtY2Q5MWY3Y2Q1NDcxIiwidCI6IjZkNDg1YWY3LTAxZjYtNGE2MC05OWEwLTQzOTQyNzJiMjUzNSJ9"
}

# Menu lateral para seleção de relatórios
with st.sidebar:
    # Adiciona logo (certifique-se de que o caminho para a logo está correto)
    st.image("caminho_para_logo.png", use_column_width=True)
    
    st.title("Navegação")
    selected = option_menu(
        menu_title=None,  # menu title
        options=list(reports.keys()),  # options
        icons=["bar-chart-fill"]*5,  # icons
        menu_icon="cast",  # menu icon
        default_index=0,  # default selected index
    )

# Exibe o relatório selecionado
show_report(reports[selected])
