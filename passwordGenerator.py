#por @otaviomuraca

# Import random
import random

# Define as classificações de caracteres:
lower = 'abcdefghijklmnopqrstuvwyxz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWYXZ'
numbers = '0123456789'
symbols = '!@#$%&*'

# Cria a lista de caracteres a ser utilizada:
characters = []

# Opções a serem escolhidas pelo usuário:
print("Vamos configurar o seu PASSWORD: ")
a = str(input("Sua senha será composta por LETRAS MINUSCULAS? <S/N>: ").upper())
b = str(input("Sua senha será composta por LETRAS MAIUSCULAS? <S/N>: ").upper())
c = str(input("Sua senha será composta por NÚMEROS? <S/N>: ").upper())
d = str(input("Sua senha será composta por SIMBOLOS? <S/N>: ").upper())

# Caso o usuário não selecione nenhuma das opções, retorna a pergunta novamente:
while a != "S" and b != "S" and c != "S" and d != "S":
  print("Favor escolher pelo menos uma das opções: ")
  a = str(input("Sua senha será composta por LETRAS MINUSCULAS? <S/N>: ").upper())
  b = str(input("Sua senha será composta por LETRAS MAIUSCULAS? <S/N>: ").upper())
  c = str(input("Sua senha será composta por NÚMEROS? <S/N>: ").upper())
  d = str(input("Sua senha será composta por SIMBOLOS? <S/N>: ").upper())

# Pergunta o número de caracteres a ser utilizado:
size = int(input("Número de caracteres da senha: "))

# Caso seja igual o menor que ZERO, repete a pergunta:
while size <= 0:
  print("O valor tem que ser maior que 0: ")
  size = int(input("Número de caracteres da senha: "))

# Configuração da lista de caracteres a ser utilizada:

# Vai utilizar caracteres minusculos?
if a == "S":
  for i in lower:
    characters.append(i)

# Vai utilizar caracteres maiusculos?
if b == "S":
  for i in upper:
    characters.append(i)

# Vai utilizar caracteres números?
if c == "S":
  for i in numbers:
    characters.append(i)

# Vai utilizar caracteres símbolos?
if d == "S":
  for i in symbols:
    characters.append(i)

# Gerador do password
password = "".join(random.choices(characters, k= size))

# Mensagem com o password gerado.
print("A senha gerada com " + str(size) + " digitos é: " +  password)

novaSenha = str(input("Gostaria de mudar a senha? <S/N>").upper())

while novaSenha == "S":
  password = "".join(random.choices(characters, k=size))
  print("A senha gerada com " + str(size) + " digitos é: " +  password)
  novaSenha = str(input("Gostaria de mudar a senha? <S/N>").upper())

save = str(input("Deseja salvar a senha? <S/N>").upper())

if save =="S":
  logPassword = {}
  logPassword[input("Nome da Senha: ")] = password
  with open("passwords.txt", "a") as log:
    log.write(str(logPassword))
