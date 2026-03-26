```Python

# src/app.py

import streamlit as st
import pandas as pd
import json
from agente import FinDataAgent  # Nosso agente que processa os dados

# -----------------------------
# Configurações da Página
# -----------------------------
st.set_page_config(
    page_title="FinData AI",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("💰 FinData AI - Seu Agente Financeiro Inteligente")
st.write(
    "Aqui você pode analisar seus dados financeiros e receber insights e recomendações personalizadas."
)

# -----------------------------
# Carregamento de Dados
# -----------------------------
@st.cache_data
def load_csv(file_path):
    return pd.read_csv(file_path)

@st.cache_data
def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Carregando dados mockados da pasta data/
transacoes = load_csv("../data/transacoes.csv")
historico = load_csv("../data/historico_atendimento.csv")
perfil = load_json("../data/perfil_investidor.json")
produtos = load_json("../data/produtos_financeiros.json")

st.sidebar.header("Dados do Cliente")
st.sidebar.write(f"Nome: {perfil.get('nome', 'Desconhecido')}")
st.sidebar.write(f"Perfil: {perfil.get('perfil', 'Desconhecido')}")
st.sidebar.write(f"Saldo disponível: R$ {perfil.get('saldo', 0):,.2f}")

# -----------------------------
# Inicialização do Agente
# -----------------------------
agent = FinDataAgent(
    perfil_investidor=perfil,
    transacoes=transacoes,
    historico_atendimento=historico,
    produtos_financeiros=produtos
)

# -----------------------------
# Interface de Chat
# -----------------------------
st.header("🗨️ Converse com seu agente")

user_input = st.text_input("Digite sua pergunta ou solicitação:")

if user_input:
    with st.spinner("Processando..."):
        response = agent.get_response(user_input)
    st.markdown("**FinData AI:**")
    st.write(response)

# -----------------------------
# Exibição de Últimas Transações
# -----------------------------
if st.checkbox("Mostrar últimas transações"):
    st.subheader("📊 Últimas transações")
    st.dataframe(transacoes.sort_values(by="data", ascending=False).head(10))
```
