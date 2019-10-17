#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:52:41 2019

@author: victor
"""
#Constantes
TAM = 30000
#Tabela Hash
def funcH(TAM, chave):
    posicao = chave % TAM
    return posicao

def inserir(vetor, chave, TAM):
    posicao = funcH(TAM, chave)
    while vetor[posicao] is not None:
        if posicao == TAM-1:
            posicao = 0
        else:
            posicao += 1
    vetor[posicao] = chave
    return

def buscar(vetor, chave, TAM):
    posicao = funcH(TAM, chave)
    while vetor[posicao] is not None:
        if chave == vetor[posicao]:
            print("\nChave encontrada na posição %d." % posicao)
            return posicao
        else:
            if posicao == TAM-1:
                posicao = 0
            else:
                posicao += 1
    print("\nChave não encontrada na tabela.")
    return 0

def imprimirHash(vetor, TAM):
    print("\nTabela Hash\n")
    for i in range(0, TAM):
        if vetor[i] is None:
            print("NULL", end = ' ')
        else:
            print("%d" % vetor[i], end = ' ')
    return

def elementosMesmoMod(vetor, chave_remover, TAM):
    contagem = 0
    mod = funcH(TAM, chave_remover)
    for i in range(0, TAM):
        if vetor[i] is not None:
            mod_i = funcH(TAM, vetor[i])
            if mod_i == mod:
               contagem += 1
        i += 1
    return contagem

def ultimoMod(vetor, chave_remover, contagem, TAM):
    mod = funcH(TAM, chave_remover)
    i = mod
    j = buscar(vetor, chave_remover, TAM)
    if j == TAM - 1:
        j = 0
    else:
        j += 1
    while i != None:
        if vetor[j] is not None:
            if i == funcH(TAM, vetor[j]):
                contagem -= 1
                if contagem == 2:
                    return j
        if j == i-1:
            i = None
            return None
        elif j == TAM-1:
            j = 0
        else:
            j += 1

          
def remocao(vetor, chave_remover, TAM):
    
    mod = funcH(TAM, chave_remover)
    contagem = elementosMesmoMod(vetor, chave_remover, TAM)
    if contagem == 1:
        vetor[mod] = None
        print("\nRemovido!")
        return vetor               
    else:
        ultimo = ultimoMod(vetor, chave_remover, contagem, TAM)
        if ultimo is None:
            vetor[mod] = None
            print("\nRemovido!")
            return vetor
        else:
            mod = buscar(vetor, chave_remover, TAM)
            vetor[mod] = vetor[ultimo]
            vetor[ultimo] = None
            return vetor

        
## =============================================================================
##Inicia contagem de tempo de execução do programa.
#start = time.time()
#end = time.time()
#print("A: %.7f" % (end - start))
## =============================================================================

# =============================================================================

with open('vetor.txt', 'r') as f:
    vetor = f.read().splitlines() 
#Converte lista de strings para int.
vetor = [int(j) for j in vetor]
    
vetor_hash = [0] * TAM

for i in range(0, TAM):
    vetor_hash[i] = None

for j in range(0, len(vetor)):
    inserir(vetor_hash, vetor[j], TAM)

buscar(vetor_hash, 999, TAM)
inserir(vetor_hash, 999, TAM)
buscar(vetor_hash, 999, TAM)
end = time.time()
#chave_remover = int(input("\nDigite a chave a ser removida: "))
if buscar(vetor_hash, 999, TAM):
    vetor_hash = remocao(vetor_hash, 999, TAM)

