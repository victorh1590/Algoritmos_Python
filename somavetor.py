# -*- coding: utf-8 -*-
"""
Spyder Editor
@author: victor
Este é um arquivo de script temporário.
"""

#Algoritmo que soma elementos de um vetor. Soma os 2 elementos mínimos sucessivamente até restar apenas um elemento.
def somaVetor(v):
    n = len(v)
    if n == 1:
        print("\n%d" % v[0])
        return
    elif n == 2:
        print("\n%d" % v[0]+v[1])
        return
    else:
         i = 0
         k = -1
         j = n-1
         
         while i != j:
             
             i += 1
             if i == n:
                 i = 0  
             k += 1
             if k == n:
                 k = 0
                 
             if v[k] == 0:
                 continue
            
             else:
                if v[i] > v[j]:
                    v[j] = v[j] + v[k]
                    v[k] = 0
                else:
                    j += 1
                    if j == n:
                        j = 0
                    v[j] = v[i]+v[k]
                    v[i] = 0
                    v[k] = 0
    
    for i in range(0, len(v)):
        print("\n%d" % v[i])
    
    for i in range(0, len(v)):
        if v[i] != 0:
            print("\nResultado: %d" % v[i])
    return 

#Início do Programa
    
with open('vetor.txt', 'r') as f:
    v = f.read().splitlines()
   
#Converte lista de strings para int.
v = [int(j) for j in v]

for i in range(0, len(v)):
    print("\n%d" % v[i])

somaVetor(v)
