#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:27:48 2019

@author: victor
"""
import time

class Node: 
    def __init__(self, chave): 
        self.chave = chave  
        self.esquerda = None
        self.direita = None

def contaNos(node, contagem):
    if node is None:
        return contagem
    else:
        contagem += 1
        contagem = contaNos(node.esquerda, contagem)
        contagem = contaNos(node.direita, contagem)
        return contagem
        
def printNumNos(node):
    contagem = contaNos(node, 0)
    if contagem == 0:
        print("\nA árvore está vazia.")
        return
#    else: 
        print("\nO número de nós na árvore é %d" % contagem)
    return    

def arvoreVazia(node):
    contagem = contaNos(node, 0)
    if contagem == 0:
        return 1
    else:
        return 0

def inserir(chave, node):
    if arvoreVazia(node):
        return Node(chave)
    elif node.chave > chave:
        node.esquerda = inserir(chave, node.esquerda)
    else:
        node.direita = inserir(chave, node.direita)
    return node

def busca(chave, node):
    i = 1
    while i != 0:
        if node is None:
            print("\nElemento não encontrado.")
            return
        else:
            if chave == node.chave:
                print("\nElemento encontrado! %d" % node.chave)
                return node
            else:
                if chave > node.chave:
                    node = node.direita
                else:
                    node = node.esquerda
    return

def imprimeArvore(node):
    if arvoreVazia(node):
        print("\nÁrvore Vazia!")
    else:
        percorreImprimindo(node)
    return

#imprime inOrder
#def percorreImprimindo(node):
#    if node is None:
#        return
#    else:
#        percorreImprimindo(node.esquerda)
#        print("%d" % node.chave, end = ' ')
#        percorreImprimindo(node.direita)
#        return
    
#imprime preOrder
def percorreImprimindo(node):
    if node is None:
        return
    else:
        print("%d" % node.chave, end = ' ')
        percorreImprimindo(node.esquerda)
        percorreImprimindo(node.direita)
        return
#Remoção
def sucessorInorder(atual):
    while atual.esquerda is not None:
        atual = atual.esquerda
    return atual

def remove(node, chave):
    if node is None:
        return node
    if chave < node.chave:
        node.esquerda = remove(node.esquerda, chave)
    elif chave > node.chave:
        node.direita = remove(node.direita, chave)
    else:
        if node.esquerda is None:
            temp = node.direita
            node = None
            return temp
        if node.direita is None:
            temp = node.esquerda
            node = None
            return temp    
        else:
            temp = sucessorInorder(node.direita)
            node.chave = temp.chave
            node.direita = remove(node.direita, temp.chave)
    return node

#Main
    
## =============================================================================
##Inicia contagem de tempo de execução do programa.
#start = time.time()
#end = time.time()
#print("A: %.7f" % (end - start))
## =============================================================================

raiz = None
with open('vetor.txt', 'r') as f:
    vetor = f.read().splitlines() 
#Converte lista de strings para int.
vetor = [int(j) for j in vetor]

for i in range(0, len(vetor)):
    raiz = inserir(vetor[i], raiz)     

#busca
#chave_buscada = int(input("\nDigite uma chave para ser buscada: "))
busca(999, raiz)
raiz = inserir(999,raiz)
#busca
#chave_buscada = int(input("\nDigite uma chave para ser buscada: "))
busca(999, raiz)
raiz = remove(raiz, 999)

