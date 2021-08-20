import streamlit as st 
from corretor import corretor

st.write("# Corretor Ortográfico")
st.write("""Ele foi desenvolvido usando artigos do site da Alura 
	e é capaz de realizar correções ortográficas simples dentro de um 
	vocabulário comum ao mundo da tecnologia.""")

texto_para_corrigir = st.text_input("""Entre uma palavra em letra minúscula 
	para ser corrigido:""")

if len(texto_para_corrigir) > 0:
	correcao = corretor(texto_para_corrigir)
	st.write(correcao)
