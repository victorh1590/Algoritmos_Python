#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:36:29 2019

@author: victor
"""

import time
import random

def mergeSort(alist):
   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1
  
def main():      
    #Arquivos - Descomente para mudar a entrada.
    #No Spyder: CTRL + 1 - Comenta ou descomenta linha.
    
#    with open('entrada10.txt', 'r') as f:
#    with open('entrada1000.txt', 'r') as f:
#    with open('entrada10000.txt', 'r') as f:
#    with open('entrada1e+05.txt', 'r') as f:
#    with open('entrada1e+06.txt', 'r') as f:
#    with open('entrada1e+07.txt', 'r') as f:
        vetor = f.read().splitlines()
    
    #Checa o tipo.  
    print(type(vetor[0]))
    
    #Converte lista de strings para int.
    vetor = [int(j) for j in vetor]
    
    #Checa de novo o tipo.
    print(type(vetor[0]))
    
    #Imprime tamanho do vetor.
    print("Tamanho(n): %d" % len(vetor))
    
    #Chama Merge Sort
    mergeSort(vetor)
    
    #Escreve arquivo de texto com conteúdo do vetor.
    f = open("vetorordenado.txt", "w")
    for i in range(0, len(vetor)):
        f.write("%d\n" % vetor[i])
    f.close()

    #Chama Merge Sort
    mergeSort(vetor)
    
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
        
    #Chama Merge Sort
    mergeSort(vetor)
     
    f = open("vetorordenado3.txt", "w")
    for i in range(0, len(vetor)):
        f.write("%d\n" % vetor[i])
    f.close()
    return 0

main()
