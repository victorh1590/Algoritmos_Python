#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Oct 10 21:58:02 2019

@author: victor
"""
  
def buscaBinaria(vetor, chave, menor, maior):  
    if menor > maior:
        print("\nElemento não encontrado.")
        return  
    selecionado = (menor + maior) / 2 
    selecionado = int(selecionado)
    if vetor[selecionado] == chave: 
        print("\nElemento %d encontrado." % chave)
        return selecionado  
    elif chave < vetor[selecionado]: 
        return buscaBinaria(vetor, chave, menor, selecionado-1)  
    else:                    
        return buscaBinaria(vetor, chave, selecionado+1, maior)  
def inserir(vetor, elemento):
    i = 0
    vetor.append(0)
    if vetor[0] >= elemento:
        vetor.insert(0, elemento)
        return vetor
    else:
        while vetor[i] < elemento:
            i += 1
        vetor.insert(i, elemento)
        return vetor

def imprimeVetor(vetor):
    for i in range(0, len(vetor)):
        print("%d" % vetor[i], end =' ')
#Main   
#Abre arquivo
with open('vetor.txt', 'r') as f:
    vetor = f.read().splitlines() 
#Converte lista de strings para int.
vetor = [int(j) for j in vetor]

chave = int(input("\nDigite elemento a ser buscado: "))
maior = len(vetor)-1
menor = vetor[0]
buscaBinaria(vetor, chave, menor, maior)
