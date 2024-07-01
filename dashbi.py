import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

# Configurar a página para o layout 'wide'
st.set_page_config(layout="wide", page_title="Dashboard", page_icon=":bar_chart:")

# Estilizar a barra lateral e o conteúdo principal para responsividade
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
    .css-12oz5g7 {
        padding-top: 2rem;
    }
    .stSidebar {
        background-color: #2e3b4e;
        width: 250px; 
    }
    .sidebar .sidebar-content {
        padding: 1rem 2rem;
    }
    .report-container {
        width: 100%;
        height: 100%;
    }
    @media (max-width: 768px) {
        .report-container iframe {
            width: 100% !important;
            height: 600px !important;
        }
    }
    @media (min-width: 769px) {
        .report-container iframe {
            width: 1200px !important;
            height: 750px !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Lista de relatórios com título e URL
reports = {
    "BIM Terraplanagem":"https://app.powerbi.com/view?r=eyJrIjoiMWU2NTNiZmEtZjU2NS00ZmY1LTk5ZTgtOTRlZjNmYmI4M2U2IiwidCI6IjZkNDg1YWY3LTAxZjYtNGE2MC05OWEwLTQzOTQyNzJiMjUzNSJ9",
    "4D e LPS": "https://app.powerbi.com/view?r=eyJrIjoiZWFiN2VlZjQtZmNkMS00YmJkLWI1MzItYjYxNDMyYjdiZjY1IiwidCI6IjZkNDg1YWY3LTAxZjYtNGE2MC05OWEwLTQzOTQyNzJiMjUzNSJ9",
    "4D e Planejamento": "https://app.powerbi.com/view?r=eyJrIjoiNWE0NjY3MjEtMTdkNi00YjAwLTg3ZjgtNmM1ZDhhMzY1MGU0IiwidCI6IjZkNDg1YWY3LTAxZjYtNGE2MC05OWEwLTQzOTQyNzJiMjUzNSJ9",
    "LPS": "https://app.powerbi.com/view?r=eyJrIjoiNDhmZmRhNzMtYzBiMS00ZjRmLThiMGUtYjc3NzkyNGRlODIwIiwidCI6IjZkNDg1YWY3LTAxZjYtNGE2MC05OWEwLTQzOTQyNzJiMjUzNSJ9",
    "Planejamento": "https://app.powerbi.com/view?r=eyJrIjoiMzBiMWI3MjQtYzQ0Zi00OWI0LTliY2ItNTAyNmQ4NzY3MzVkIiwidCI6IjZkNDg1YWY3LTAxZjYtNGE2MC05OWEwLTQzOTQyNzJiMjUzNSJ9",
    
}

# Função para exibir cada relatório
def show_report(url):
    st.markdown(f"""
        <div class="report-container">
            <iframe src="{url}" width="100%" height="750" frameborder="0" allowfullscreen></iframe>
        </div>
        """, unsafe_allow_html=True)

# Barra lateral
with st.sidebar:
    st.title("Dashboard de Navegação")
    selected = option_menu(
        menu_title=None,  # Título do menu
        options=list(reports.keys()),  # Opções
        icons=["bar-chart-fill"] * len(reports),  # Ícones
        menu_icon="cast",  # Ícone do menu
        default_index=0,  # Índice selecionado por padrão
    )
    
    st.markdown(
        """
        <div style="padding: 20px 10px; color: #f2f2f2;">
            <p>Selecione um relatório para visualização detalhada.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.image("caminho_para_logo.png", use_column_width=True)

# Exibe o relatório selecionado
show_report(reports[selected])
