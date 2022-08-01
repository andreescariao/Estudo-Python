# Dictionary
carro={
    "FABRICANTE":"HONDA",
    "MODELO":"HRV",
    "ANO":"2016",
    "COR":"PRATA"
}

print(carro["FABRICANTE"])

# Adicionar elemento
carro["CAMBIO"]="AUTOMATICO"

# Tamanho do dicionário
print("Tamanho do dicionário: "+str(len(carro)))

# Imprime matriz com chave e valores
for c,v in carro.items():
    print(c+": "+v)

# Remover chave
carro.pop("CAMBIO")
