#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:29:05 2019

@author: victor
"""
#Algoritmo para descobrir maior e segundo maior elementos de um vetor.

def max2x(v):
    n = len(v)
    
    if n == 1:
        max1 = v[0]
        max2 = v[0]
    else:
        max1 = v[1]
        max2 = v[0]
    
    i = 3
    while i < n:
        if max1 < v[i]:
            max1 = v[i]
        if max2 < v[i-1]:
            max2 = v[i-1]
        i += 2
        
    if (n % 2) == 1:
        if v[n-1] > max2:
            max2 = v[n-1]
    
    if max1 < max2:
        aux = max1
        max1 = max2
        max2 = aux
    
    print("Maior: {0}\nSegundo Maior: {1}".format(max1, max2))
        
#Início do Programa
    
with open('vetor.txt', 'r') as f:
    v = f.read().splitlines()
   
#Converte lista de strings para int.
v = [int(j) for j in v]

for i in range(0, len(v)):
    print("%d " % v[i])

print("\n")
max2x(v)


