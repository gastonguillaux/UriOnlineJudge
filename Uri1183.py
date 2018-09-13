# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 22:55:18 2018

@author: Gaston Guillaux
"""

#variaveis iniciais
operacao = input()
matrix = []
aux = []

#forma matriz
for x in range(144):
    num = float(input())
    aux.append(num)
    if (x+1) % 12 == 0:
        matrix.append(aux)
        aux = []

y = 1
soma = 0
count = 0
for linha in matrix:
    for x, n in enumerate(linha):
        if x >= y:
            soma += n
            count += 1
    y += 1

if operacao == 'S':
    print(round(soma,1))
elif operacao == 'M':
    print(round(soma/66),1)
        