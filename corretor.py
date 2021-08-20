import nltk

def separa_palavras(lista_tokens):
    
    lista_palavras = []
    
    for token in lista_tokens:
        if token.isalpha():
            lista_palavras.append(token)
    
    return lista_palavras

def normalizacao(lista_palavras):
    
    lista_normalizada = []
    
    for palavra in lista_palavras:
        lista_normalizada.append(palavra.lower())
    
    return lista_normalizada

def insere_letras(fatias):
    
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    
    return novas_palavras

def deletando_caracteres(fatias):
    novas_palavras = []
    
    for E, D in fatias:
        novas_palavras.append(E + D[1:])
    
    return novas_palavras

def troca_letras(fatias):
    
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D[1:])
    
    return novas_palavras

def inverte_letras(fatias):
    novas_palavras = []
    
    for E, D in fatias:
        if len(D) > 1:
            novas_palavras.append(E + D[1] + D[0] + D[2:])
    
    return novas_palavras

def gerador_palavras(palavra):    
    fatias = []
    
    for i in range(len(palavra) + 1):
        fatias.append((palavra[:i], palavra[i:]))
    
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracteres(fatias)
    palavras_geradas += troca_letras(fatias)
    palavras_geradas += inverte_letras(fatias)
    
    return palavras_geradas

def probabilidade(palavra_gerada):
    return frequencia[palavra_gerada]/total_palavras

def corretor(palavra):
    palavras_geradas = gerador_palavras(palavra)
    
    palavra_correta = max(palavras_geradas, key=probabilidade)
    
    if (palavra_correta in vocabulario):
    	return palavra_correta
    else:
    	return f"Desculpe! Corrigir a palavra '{palavra}' está além das minhas capacidades."

with open("corretor-master/artigos.txt", "r", encoding="utf-8") as f:
    artigos = f.read()

lista_tokens = nltk.tokenize.word_tokenize(artigos)
lista_palavras = separa_palavras(lista_tokens)
lista_normalizada = normalizacao(lista_palavras)
total_palavras = len(lista_normalizada)
frequencia = nltk.FreqDist(lista_normalizada)
vocabulario = set(lista_normalizada)