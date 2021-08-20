import streamlit as st 
from corretor import corretor

st.write("# Corretor Ortográfico")
st.write("""Ele foi desenvolvido usando artigos do site da Alura 
	e é capaz de realizar correções ortográficas simples dentro de um 
	vocabulário comum ao mundo da tecnologia.""")

texto_para_corrigir = st.text_input("""Insira uma palavra para ser corrigida:""")
texto_para_corrigir = texto_para_corrigir.lower()

if len(texto_para_corrigir) > 0:
	correcao = corretor(texto_para_corrigir)
	if correcao == texto_para_corrigir:
		texto_retorno = f"A palavra ' {texto_para_corrigir} ' está escrita corretamente!"
	else:
		if not correcao: # Se não tiver correção
			texto_retorno = f"Desculpe! Corrigir a palavra ' {texto_para_corrigir} ' está além das minhas capacidades."
		else:
			texto_retorno = f"A versão corrigida mais provável dessa palavra é ' {correcao} '." 

	st.write(texto_retorno)
