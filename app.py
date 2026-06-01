import streamlit as st
import pandas as pd
import joblib

# Configuração da página
st.set_page_config(
    page_title="SpaceGuard AI",
    page_icon="🚀",
    layout="centered"
)

# Estilo visual (CSS simples)
st.markdown("""
    <style>
        /* Fundo estilo espaço */
        .stApp {
            background: radial-gradient(circle at top, #0b0f1a, #05060a, #000000);
            background-attachment: fixed;
        }

        /* Título */
        h1 {
            color: #00d4ff;
            text-align: center;
            text-shadow: 0px 0px 15px #00d4ff;
        }

        /* Subtítulo */
        h2, h3, h4, p {
            color: #e6f1ff;
        }

        /* Botão mais escuro e elegante */
        .stButton > button {
            background: linear-gradient(90deg, #003b66, #001f33);
            color: white;
            font-weight: bold;
            border-radius: 12px;
            height: 3em;
            width: 100%;
            border: 1px solid #00d4ff;
            box-shadow: 0px 0px 10px rgba(0, 212, 255, 0.3);
            transition: 0.2s;
        }

        .stButton > button:hover {
            background: linear-gradient(90deg, #005a99, #002b4d);
            transform: scale(1.02);
        }

        /* Inputs */
        input {
            background-color: rgba(255,255,255,0.05) !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Título
st.title("🚀 SpaceGuard AI")
st.subheader("Classificação de Eventos Naturais com Dados da NASA")

# Carregar modelo
modelo = joblib.load("spaceguard_model.pkl")

classes = {
    0: "Sea and Lake Ice",
    1: "Severe Storms",
    2: "Volcanoes",
    3: "Wildfires"
}

st.markdown("---")

# Layout em colunas (melhor UX)
col1, col2, col3 = st.columns(3)

with col1:
    latitude = st.number_input("🌍 Latitude")

with col2:
    longitude = st.number_input("🌍 Longitude")

with col3:
    magnitude = st.number_input("💥 Magnitude", value=0.0)

col4, col5, col6, col7 = st.columns(4)

with col4:
    ano = st.number_input("📅 Ano", value=2025)

with col5:
    mes = st.number_input("📅 Mês", value=1)

with col6:
    dia = st.number_input("📅 Dia", value=1)

with col7:
    hora = st.number_input("⏰ Hora", value=12)

st.markdown("---")

# Botão central
if st.button("🚀 Realizar Previsão"):

    entrada = pd.DataFrame({
        "latitude": [latitude],
        "longitude": [longitude],
        "magnitude": [magnitude],
        "ano": [ano],
        "mes": [mes],
        "dia": [dia],
        "hora": [hora]
    })

    previsao = modelo.predict(entrada)
    categoria = classes[int(previsao[0])]

    st.success(f"🌌 Categoria prevista: **{categoria}**")

    st.balloons()
