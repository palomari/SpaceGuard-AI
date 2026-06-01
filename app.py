import streamlit as st
import pandas as pd
import joblib

# Configuração da página
st.set_page_config(
    page_title="SpaceGuard AI",
    page_icon="🚀",
    layout="wide"
)

# ====== ESTILO VISUAL ======
st.markdown("""
<style>
/* fundo geral */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top, #0b0f1a, #05060a);
    color: white;
}

/* título */
h1 {
    text-align: center;
    color: #00d9ff;
    font-size: 42px;
    text-shadow: 0px 0px 20px #00d9ff;
}

/* cards */
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 15px rgba(0,217,255,0.2);
    backdrop-filter: blur(10px);
}

/* botão */
.stButton > button {
    background: linear-gradient(90deg, #00d9ff, #0066ff);
    color: white;
    font-weight: bold;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    border: none;
}
.stButton > button:hover {
    transform: scale(1.02);
    transition: 0.2s;
}
</style>
""", unsafe_allow_html=True)

# ====== MODELO ======
modelo = joblib.load("spaceguard_model.pkl")

classes = {
    0: "Sea and Lake Ice ❄️",
    1: "Severe Storms 🌪️",
    2: "Volcanoes 🌋",
    3: "Wildfires 🔥"
}

# ====== HEADER ======
st.title("🚀 SpaceGuard AI")
st.markdown("### 🌍 Sistema inteligente de detecção de eventos naturais baseado em dados da NASA")
st.markdown("---")

# ====== LAYOUT ======
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("## 📡 Entrada de Dados")

    latitude = st.number_input("Latitude 🌍")
    longitude = st.number_input("Longitude 🌍")
    magnitude = st.number_input("Magnitude 💥", value=0.0)

    ano = st.number_input("Ano 📅", value=2025)
    mes = st.number_input("Mês 📅", value=1)
    dia = st.number_input("Dia 📅", value=1)
    hora = st.number_input("Hora ⏰", value=12)

    prever = st.button("🚀 Executar Análise")

with col2:
    st.markdown("## 📊 Painel de Resultados")

    st.markdown("""
    <div class="card">
        <h3>🌌 Sistema SpaceGuard AI</h3>
        <p>Insira os dados ao lado e execute a análise para detectar eventos naturais em tempo real.</p>
    </div>
    """, unsafe_allow_html=True)

    if prever:
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

        st.markdown("### 🔮 Resultado da Análise")
        st.success(f"🌠 Evento detectado: **{categoria}**")

        st.markdown("""
        <div class="card">
            <h4>🛰️ Status do Sistema</h4>
            <p>✔ Dados processados com sucesso</p>
            <p>✔ Modelo de IA ativado</p>
            <p>✔ Classificação concluída</p>
        </div>
        """, unsafe_allow_html=True)

        st.balloons()
