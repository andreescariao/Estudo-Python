# Listas
from turtle import clear
carros=["HRV","Golf","Argo","Focus"]
print(carros)

# Subistituir na Lista
carros[3]="Fusion"
print(carros)

# Método Append - adicionar novos itens na lista
carros.append("Fiat")
carros.append("Polo")
print(carros)

# Imprimir numero da lista com método len
print("Numero de carros na lista: "+str(len(carros)))

# Remover carro da lista
carros.remove("Fusion")
print(carros)
print("Numero de carros na lista: "+str(len(carros)))

# Remove o último elemento da lista
carros.pop()
print(carros)
print("Numero de carros na lista: "+str(len(carros)))

# Remove número do carro da lista
del carros[2]
print(carros)
print("Numero de carros na lista: "+str(len(carros)))

# Limpa todos os elementos da lista
carros.clear()
print(carros)
print("Numero de carros na lista: "+str(len(carros)))

# Copiar uma lista para outra
carros=["Lista","de","Carros"]
carros2=list(carros)
print("Lista Carros 2: "+ str(carros2))
print("Número na lista 2: "+str(len(carros2)))
