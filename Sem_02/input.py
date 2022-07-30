# Biblioteca os para usar o comando cls e limpar terminal
import os
os.system('cls')

# Input
nome=input("Digite seu nome: ")
print("Nome Digitado: "+nome)

# Input com operação de casting para converter para inteiro
num1=int(input("Digite o 1 numero:"))
num2=int(input("Digite o 2 numero:"))
res=num1+num2
print("Soma dos valores: "+str(res))
