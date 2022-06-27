#!/usr/bin/env python
# coding: utf-8

# ### 01 - Teste de gravidez
# Escreva uma célula com controle de fluxos que tem como premissa a existência das seguintes variáveis:
# 
# - ```sexo``` como ```str``` indicando os valores '**M**' para masculino e '**F**' para feminino  
# - ```beta_hcg``` que indica a quantidade do beta-HCG no sangue em mUI/mL.
# 
# A sua tarefa é escrever um código que imprima como resultado "indivíduo do sexo masculino" quando sexo = 'M', caso sexo = 'F', se o valor de beta-HCG for maior que 5, retorne "Positivo" indicando que a paciente está grávida, e retorne "Negativo" caso contrário.
# 
# Não mexa nos valores da variável ```sexo``` nem em ```beta_hcg```, e escreva um código que funcione para quaisquer valores possíveis de ambos: ```sexo``` = '**M**' ou '**F**' e ```beta_hcg``` assumindo valores inteiros positivos.

# In[269]:


sexo = 'M'
beta_hcg = 6

# seu código vem abaixo desta linha

if sexo == 'M':
    print('Paciente de sexo MASCULINO. \nResultado NEGATIVO.')
else:
    if beta_hcg > 5:
        print(f'Paciente do sexo FEMININO e beta-HCG foi {beta_hcg}. \nResultado: POSITIVO.')
    else: 
        print(f'Paciente do sexo FEMININO e beta-HCG foi {beta_hcg}. \nResultado: NEGATIVO.')


# ### 02 - Renomeando variáveis
# 
# Vamos ver adiante que uma forma de renomear variáveis de um conjunto de dados é através de dicionários - o dicionário deve conter como chave o nome original, associando a cada chave um único valor (tipo *str*) que contenha o nome novo.
# 
# A sua tarefa é escrever um dicionário que possa ser utilizado para traduzir as variáveis ```name``` (nome), ```age``` (idade) e ```income``` (renda). Ou seja, esse dicionário deve relacionar as chaves *name, age* e *income* às suas respectivas traduções.

# In[270]:


dic_renomeacao = {'name': 'nome', 'age':'idade', 'income':'renda'}
dic_renomeacao


# ### 03 - É divisível?
# A sua tarefa é escrever um código que indique se um número ```N``` é divisível por um número P. Escreva um programa que faça essa verificação para quaisquer combinações de ```N``` e ```M``` e devolva uma mensagem indicativa no output.

# In[271]:


N = 200
M = 5

#Seu código

if (N%M) >= 1:
    print(f'A divisão entre {N} e {M} não foi válida.')
else: 
    print(f'A divisão entre {N} e {M} foi de {int(N/M)}.')


# ### 04 - Números primos
# > Um número **N** é primo se e somente se é divisível por 1, -1, por **N** e por -**N**.  
# 
# Escreva um script que verifica se ```N``` é um número primo, verificando se ```N``` é divisível por todos os números de ```1``` a ```N-1```. Você vai precisar usar alguma ferramenta de *loop* que você aprendeu para isto. No final, devolva uma mensagem no output indicando se o número é primo ou não.

# In[272]:


N = 10

# seu código abaixo
count = 0
for i in range(1, N -1):
    if N % i == 0:
        count += 1
        break
        
if count == 1:
    print(f"O número {N} é primo!")
    
elif N == 2: #inseri essa regra por causa do -1 no range.
    print(f"O número {N} é primo!") 
    
else:
    print(f"O número {N} NÃO É primo!")
    


# ### 05 - Desafio
# O algorítmo do exercício anterior não é o mais eficiente. O que você pode fazer para deixá-lo mais eficiente? Ou seja, executar menos comparações, portanto consumir menos tempo.
# 1. Será que precisamos correr o loop até o final sempre?
# 2. Será que precisamos mesmo verificar **todos** os números?
# 3. Será que precisamos ir até N-1?
# 
# Essas perguntas levam ao tipo de pensamento voltado a deixar um algoritmo mais eficiente. Veja se você consegue melhorar o seu.

# In[273]:


N = 98

# seu código abaixo
count = 0
for i in range(1, N -1):
    if N % i == 0:
        count += 1
        
if count == 1:
    print(f"O número {N} é primo!")
elif N == 2: #inseri essa regra por causa do -1 no range.
    print(f"O número {N} é primo!") 
else:
    print(f"O número {N} NÃO É primo!")



# ### 06 - Peso ideal 1
# O IMC (índice de massa corpórea) é um indicador de saúde mais bem aceito que o peso. Ele é calculado como:
# 
# $$ IMC = \dfrac{peso}{altura^2}$$
# 
# Segundo a OMS, valores *normais* são entre 18.5 e 24.9.
# 
# Sua tarefa é encontrar o ponto médio dessa faixa.

# In[274]:


def rangeFloat(start, stop, step):
    x = start
    while x <= stop:
        yield x
        x = x + step
        
steps = rangeFloat(18.5, 24.9, 0.1)

final = 0
itens = 0
for i in steps:
    final += i
    itens += 1

media = final/itens
print(f'{media:.2f}')
imc_ideal = media


# In[ ]:





# In[ ]:





# ### 07 - Peso ideal 2
# Recebendo um valor de altura, encontre o peso '*ideal*' dessa pessoa, que fornece o IMC encontrado acima

# In[275]:


altura = 1.70

# Seu código
peso_ideal = (altura ** 2) * imc_ideal
peso_ideal


# ### 08 - Peso ideal 3
# Dada uma lista contendo as alturas de pacientes, crie uma nova lista que contenha o peso '*ideal*' (que fornece o IMC calculado em **Peso ideal 1**) desses pacientes.

# In[276]:


lista_alturas = [1.95, 2.05, 1.70, 1.65]

lista_peso_ideal = []

# seu código

for i in lista_alturas: 
    resultado = (i ** 2) * imc_ideal
    lista_peso_ideal.append(resultado)


lista_peso_ideal


# ### 09 - Peso ideal 4
# Dada uma lista de tuplas - cada elemento da lista é uma tupla contendo altura e peso de um paciente - crie uma nova lista com o IMC desses pacientes.

# In[277]:


altura_peso = [(1.80, 90), (1.65, 75), (1.91, 70)]

imc = []

# seu código

for i in altura_peso: 
        calculo = i[1] / (i[0] ** 2)
        imc.append(calculo)
        

imc


# ### 10 - Peso ideal 5
# Dada uma lista de **listas** - cada elemento da lista é uma **lista** contendo altura e peso de um paciente, adicione mais um elemento à lista de cada paciente contendo o IMC do paciente. Verifique também se é 'baixo', 'normal' ou 'alto' segundo os padrões da OMS em que normal é entre 18.5 e 24.9.
# 
# Reflexão: por que no problema anterior temos que criar uma nova lista, e não podemos adicionar os dados de cada indivíduo à tupla?

# In[278]:


altura_peso = [[1.80, 90], [1.65, 75], [1.91, 70]]

# seu código

for i in altura_peso:
    i.append(i[1] / (i[0]**2))


altura_peso


# ### Eu não consegui transformar dados FLOAT em round(2) para minimizar as casas decimais. 
# ### Até tentei em converter, mas não aceitou o formato dentro de LISTA. 
# ### Pode me dar uma dica? 

# In[ ]:





# In[ ]:
 



