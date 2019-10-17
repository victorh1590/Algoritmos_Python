#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:18:38 2019

@author: victor
"""

import time

def shell(vetor):
    h = 1
    while h <= len(vetor):
        h = 3*h+1
    while h >= 1:
        h = h/3
        h = int(h)
        for i in range(h, len(vetor)):
            valor = vetor[i]
            j = i-h
            while j >= 0 and valor < vetor[j]:
                vetor[j+h] = vetor[j]
                j = j-h
            vetor[j+h] = valor
            
    
def main():      
    #Arquivos - Descomente para mudar a entrada.
    #No Spyder: CTRL + 1 - Comenta ou descomenta linha.
    
    with open('entrada10.txt', 'r') as f:
#    with open('entrada1000.txt', 'r') as f:
#    with open('entrada10000.txt', 'r') as f:
#    with open('entrada1e+05.txt', 'r') as f:
#    with open('entrada1e+06.txt', 'r') as f:
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
     
    #Chama Insertion Sort
    shell(vetor)
    
    #Escreve arquivo de texto com conteúdo do vetor.
    f = open("vetorordenado.txt", "w")
    for i in range(0, len(vetor)):
        f.write("%d\n" % vetor[i])
    f.close()
     
    #Chama Insertion Sort
    shell(vetor)
    
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

    #Chama Insertion Sort
    shell(vetor)

    f = open("vetorordenado3.txt", "w")
    for i in range(0, len(vetor)):
        f.write("%d\n" % vetor[i])
    f.close()
    return 0

main()
