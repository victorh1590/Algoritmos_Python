#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:08:29 2019

@author: victor
"""

import time

def selection(vetor):
    for i in range(0, len(vetor)):
        min_index = i
        for j in range(i+1, len(vetor)):
            if vetor[min_index] > vetor[j]:
                min_index = j
        temp = vetor[i]
        vetor[i] = vetor[min_index]
        vetor[min_index] = temp
 
def main():      
    #Arquivos - Descomente para mudar a entrada.
    #No Spyder: CTRL + 1 - Comenta ou descomenta linha.
    
#    with open('entrada10.txt', 'r') as f:
#    with open('entrada1000.txt', 'r') as f:
#    with open('entrada10000.txt', 'r') as f:
#    with open('entrada1e+05.txt', 'r') as f:
    #with open('entrada1e+06.txt', 'r') as f:
    #with open('entrada1e+07.txt', 'r') as f:
        vetor = f.read().splitlines()
    
    #Checa o tipo.  
    print(type(vetor[0]))
    
    #Converte lista de strings para int.
    vetor = [int(j) for j in vetor]
    
    #Checa de novo o tipo.
    print(type(vetor[0]))
    
    #Imprime tamanho do vetor.
    print("Tamanho(n): %d" % len(vetor))
     
    #Chama Selection Sort
    selection(vetor)

    #Escreve arquivo de texto com conteúdo do vetor.
    f = open("vetorordenado.txt", "w")
    for i in range(0, len(vetor)):
        f.write("%d\n" % vetor[i])
    f.close()

    #Chama Selection Sort
    selection(vetor)
     
    #Escreve arquivo de texto com conteúdo do vetor.
    f = open("vetorordenado2.txt", "w")
    for i in range(0, len(vetor)):
        f.write("%d\n" % vetor[i])
    f.close()
    
    vetor.reverse()
    
    f = open("vetorinvertido.txt", "w")
    for i in range(0, len(vetor)):
        f.write("%d\n" % vetor[i])
    f.close()

    #Chama Selection Sort
    selection(vetor)
    
    f = open("vetorordenado3.txt", "w")
    for i in range(0, len(vetor)):
        f.write("%d\n" % vetor[i])
    f.close()
    return 0

main()
