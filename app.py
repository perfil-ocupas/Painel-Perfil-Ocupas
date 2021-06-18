import streamlit as st
import pandas as pd
import numpy as np
# import plotly.express as px

dados = pd.read_csv('dados/9deJulho_reduzido.csv')
ocupacao = st.selectbox("Selecione a Ocupação: ", ["Todas"] + list(dados["Ocupacao"].unique()))
st.dataframe(dados)
# import pdb; pdb.set_trace()


# session_state.escola = st.selectbox(
#     "Selecione a Ocupação: ",
#     ["", "Minha escola não está na lista"] + list(data["codinep_nomedaescola"]),
# )
# if ocupacao != "Todas":
#     dados = dados[dados.Ocupacao == ocupacao]
# x = st.slider('Select a value')
# st.write(x, 'squared is', x * x)