#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 08:48:39 2019

@author: victor
"""

import time

def insertion(vetor):
    for i in range(0, len(vetor)):
        j = i-1
        x = vetor[i]
        while x < vetor[j] and j >= 0:
            vetor[j+1] = vetor[j]
            vetor[j] = x
            j = j-1
 
def main(): 
           
    #Arquivos - Descomente para mudar a entrada.
    #No Spyder: CTRL + 1 - Comenta ou descomenta linha.
    
#    with open('entrada10.txt', 'r') as f:
#    with open('entrada1000.txt', 'r') as f:
#    with open('entrada10000.txt', 'r') as f:
    with open('entrada1e+05.txt', 'r') as f:
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

    #Chama Insertion Sort
    insertion(vetor)
     
    #Escreve arquivo de texto com conteúdo do vetor.
    f = open("vetorordenado.txt", "w")
    for i in range(0, len(vetor)):
        f.write("%d\n" % vetor[i])
    f.close()
    
    #Chama Insertion Sort
    insertion(vetor)
      
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
    insertion(vetor)
  
    f = open("vetorordenado3.txt", "w")
    for i in range(0, len(vetor)):
        f.write("%d\n" % vetor[i])
    f.close()
    return 0

main()
