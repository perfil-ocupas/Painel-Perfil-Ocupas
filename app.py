import streamlit as st
import pandas as pd
import numpy as np

dados = pd.read_csv('dados/9deJulho_reduzido.csv')
ocupacao = st.selectbox("Selecione a Ocupação: ",["Todas", list(dados["Ocupacao"]),)
if ocupacao != "Todas":
    dados = dados[dados.Ocupacao == ocupacao]
# import pdb; pdb.set_trace()
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)