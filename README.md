# 🚀 SpaceGuard AI

### Monitoramento Inteligente de Eventos Naturais com Dados Orbitais da NASA

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest%20%7C%20XGBoost-green)
![NASA](https://img.shields.io/badge/Data-NASA%20EONET-red)
![SHAP](https://img.shields.io/badge/Explainability-SHAP-orange)
![Streamlit](https://img.shields.io/badge/Deploy-Streamlit-ff4b4b)

---

# 🌍 Sobre o Projeto

O **SpaceGuard AI** é uma plataforma desenvolvida para monitoramento inteligente de eventos naturais utilizando dados orbitais disponibilizados pela NASA.

O projeto foi desenvolvido no contexto da **Economia Espacial**, aplicando técnicas de Inteligência Artificial e Machine Learning para transformar dados gerados por satélites em informações úteis para monitoramento ambiental e tomada de decisão.

Atualmente, milhares de eventos naturais são detectados diariamente por sistemas espaciais. O acompanhamento manual dessas informações pode ser lento e sujeito a erros. O SpaceGuard automatiza esse processo através de modelos preditivos capazes de classificar eventos naturais com alta precisão.

---

# 🎯 Objetivos

O projeto possui os seguintes objetivos:

✅ Coletar dados reais da NASA através da API EONET

✅ Construir um pipeline completo de Machine Learning

✅ Aplicar e comparar diferentes algoritmos de classificação

✅ Interpretar as previsões utilizando SHAP

✅ Disponibilizar uma aplicação web para utilização prática

---

# 🛰️ Fonte dos Dados

Os dados foram obtidos através da API oficial da NASA EONET (Earth Observatory Natural Event Tracker).

Fonte:

https://eonet.gsfc.nasa.gov/api/v3/events

A API disponibiliza informações sobre eventos naturais observados por satélites ao redor do mundo.

---

# 📊 Dataset

Após a coleta e processamento dos dados foram obtidos:

| Métrica | Valor |
|----------|----------|
| Registros coletados | 7.216 |
| Variáveis | 10 |
| Fonte | NASA EONET |
| Tipo de problema | Classificação |

---

## Distribuição das Categorias

| Categoria | Quantidade |
|------------|------------|
| Wildfires | 6.635 |
| Sea and Lake Ice | 534 |
| Volcanoes | 32 |
| Severe Storms | 15 |

### Observação

O conjunto de dados apresenta forte desbalanceamento entre as categorias, com predominância de eventos classificados como **Wildfires**.

Apesar disso, os modelos apresentaram excelente desempenho na classificação dos eventos disponíveis.

---

# ⚙️ Pipeline de Machine Learning

O projeto foi desenvolvido seguindo todas as etapas do ciclo de Machine Learning.

## 1️⃣ Coleta dos Dados

- Consumo da API NASA EONET
- Extração dos eventos naturais
- Conversão para DataFrame Pandas

## 2️⃣ Pré-processamento

- Tratamento de valores ausentes
- Conversão de datas
- Padronização dos dados

## 3️⃣ Engenharia de Atributos

Foram criadas as seguintes variáveis:

- Ano
- Mês
- Dia
- Hora

Além disso, as categorias foram codificadas utilizando LabelEncoder.

## 4️⃣ Divisão dos Dados

Treinamento:

- 80% dos dados

Teste:

- 20% dos dados

---

# 🤖 Modelos Utilizados

Foram avaliados dois algoritmos estudados durante a disciplina.

## 🌲 Random Forest

Modelo baseado em múltiplas árvores de decisão.

### Resultado

Accuracy:

**99,93%**

---

## ⚡ XGBoost

Modelo baseado em Gradient Boosting.

### Resultado

Accuracy:

**99,93%**

---

# 📈 Comparação dos Resultados

| Modelo | Accuracy |
|----------|----------|
| Random Forest | 99,93% |
| XGBoost | 99,93% |

Ambos os modelos apresentaram desempenho extremamente elevado na classificação dos eventos naturais monitorados pela NASA.

---

# 🏆 Modelo Selecionado

O modelo escolhido para deploy foi o **Random Forest**.

Motivos da escolha:

- Excelente desempenho
- Menor complexidade computacional
- Maior facilidade de interpretação
- Resultado equivalente ao XGBoost

---

# 🔍 Interpretabilidade com SHAP

Para compreender como o modelo realiza suas previsões foi utilizada a biblioteca **SHAP (SHapley Additive Explanations)**.

A análise permitiu identificar quais variáveis possuem maior influência na tomada de decisão do modelo.

### Principais Variáveis

🥇 Latitude

🥈 Hora

🥉 Magnitude

Esses atributos apresentaram maior impacto na classificação dos eventos naturais.

---

# 💻 Deploy da Aplicação

Foi desenvolvida uma aplicação web utilizando **Streamlit**.

A aplicação permite que o usuário informe características de um evento natural e obtenha uma previsão automática da categoria correspondente.

### Tecnologias Utilizadas

- Streamlit
- Python
- Scikit-Learn
- Random Forest

### Aplicação

🔗 Inserir link após publicação no Streamlit Community Cloud

---

# 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- XGBoost
- SHAP
- Joblib
- Streamlit
- NASA EONET API

---

# ▶️ Como Executar Localmente

Clone o repositório:

```bash
git clone https://github.com/palomari/SpaceGuard-AI.git
```

Acesse a pasta:

```bash
cd SpaceGuard-AI
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
streamlit run app.py
```

---

# 📁 Estrutura do Projeto

```text
SpaceGuard-AI/
│
├── GenerativeAIForEngineering.ipynb
├── app.py
├── spaceguard_model.pkl
├── requirements.txt
└── README.md
```

---

# 👩‍💻 Equipe

| Integrante | RM |
|------------|------------|
| Julia Ortiz | RM550204 |
| Julia Palomari | RM551910 |
| Leticia Baptista | RM550289 |
| Vinicius Borges | RM977767 |

---

# 🎓 Disciplina

**Generative AI For Engineering**

Projeto desenvolvido para aplicação prática de Inteligência Artificial e Machine Learning no contexto da Economia Espacial.

---

# 🚀 SpaceGuard AI

### Transformando dados espaciais em inteligência para monitoramento ambiental global.
