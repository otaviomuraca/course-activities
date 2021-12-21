# -*- coding: utf-8 -*-
"""Calculadora.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bS4jZ92c83szJ_Li7x0jeSfd0A_wzayf

#####Criado por **Otavio Muraca**
"""

import pandas as pd
import math

print("--------CALCULADORA--------")
print("\n===========================")

#INSIRA O PRIMEIRO NUMERO
print('NUMERO A:')
num1 = int(input())

#SALVA O NUMERO NA MEMORIA
memoria = int(num1)

#OPERACAO A SER UTILIZADA
print('\nQUAL OPERAÇÃO VOCÊ DESEJA REALIZAR:')
print('\n1. +')
print('\n2. -')
print('\n3. /')
print('\n4. *')
print('\n5. %')

operacao = int(input())


##SEGUNDO NUMERO
print('\nNUMERO B:')
num2 = int(input())

if operacao == 1:
  memoria = (num1 + num2)
  print("\n===========================")
  print('Seu resultado é %s.' % memoria)
  print("\n===========================")

elif operacao == 2:
  memoria = (num1 - num2)
  print("\n===========================")
  print('Seu resultado é %s.' % memoria)
  print("\n===========================")

elif operacao == 3:
  memoria = (num1 / num2)
  print("\n===========================")
  print('Seu resultado é %s.' % memoria)
  print("\n===========================")

elif operacao == 4:
  memoria = (num1 * num2)
  print("\n===========================")
  print('Seu resultado é %s.' % memoria)
  print("\n===========================")

elif operacao == 5:
  memoria = (num1/100)*num2
  print("\n===========================")
  print('Seu resultado é %s.' % memoria)
  print("\n===========================")
    
else:
  print('Operação Invalida!')
  print('\n escolha uma operação da lista!')
  print("\n===========================")
