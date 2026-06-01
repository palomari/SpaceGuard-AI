
import streamlit as st
import pandas as pd
import joblib

modelo = joblib.load("spaceguard_model.pkl")

classes = {
    0: "Sea and Lake Ice",
    1: "Severe Storms",
    2: "Volcanoes",
    3: "Wildfires"
}

st.title("🚀 SpaceGuard AI")
st.subheader("Classificação de Eventos Naturais com Dados da NASA")

latitude = st.number_input("Latitude")
longitude = st.number_input("Longitude")
magnitude = st.number_input("Magnitude", value=0.0)

ano = st.number_input("Ano", value=2025)
mes = st.number_input("Mês", value=1)
dia = st.number_input("Dia", value=1)
hora = st.number_input("Hora", value=12)

if st.button("Realizar Previsão"):

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

    st.success(f"Categoria prevista: {categoria}")
