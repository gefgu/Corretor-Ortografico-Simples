import streamlit as st 
from corretor import corretor

st.write("# Corretor Ortográfico")
st.write("""Ele foi desenvolvido usando artigos do site da Alura 
	e é capaz de realizar correções ortográficas simples dentro de um 
	vocabulário comum ao mundo da tecnologia.""")

texto_para_corrigir = st.text_input("""Insira uma palavra para ser corrigido:""")
texto_para_corrigir = texto_para_corrigir.lower()

if len(texto_para_corrigir) > 0:
	correcao = corretor(texto_para_corrigir)
	if correcao == texto_para_corrigir:
		texto_retorno = "A palavra está escrita corretamente"
	else:
		texto_retorno = f"A versão corrigida dessa palavra é '{correcao}'" 

	st.write(texto_retorno)
