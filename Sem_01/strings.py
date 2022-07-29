# Strings
from pydoc import stripid
curso =" Engenharia Elétrica "

#string como vetor
print(curso[0:11])

#tamanho da string
print("Tamanho: "+str(len(curso)))

#Strip - tirar espaços (no início e final) da string
print(curso.strip())

# Função in e not in: Verificar se existe palavra dentro da string
res="python" in curso
print(res)
res="Engenharia" in curso
print(res)
res="Engenharia" not in curso
print(res)
