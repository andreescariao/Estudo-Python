# Loop For
carros=["HRV","Fiat","Golf","Audi"]
for x in carros:
    print(x)
    if x=="Golf":
        print("--------")

# Percorre cada elemento
for x in "Engenhari Elétrica":
    print(x)

# Com Break
for x in carros:
    if x=="Golf":
        break
    print(x)
