# Estrutura If Else
a=True;b=False
if a:
    print("Verdadeiro")
else:
    print("Falso")
if b:
    print("Verdadeiro")
else:
    print("Falso")

# Com operações
a=10;b=5;res=0;op="+"
if op=="+":
    res=a+b
elif op=="-":
    res=a-b
elif op=="*":
    res=a*b
elif op=="/":
    res=a/b
else:
    print("Operador inválido")
print("Operação: "+op+"\nresultado: "+str(res))

#---------------------------------------------------

clima="sol";luga="";dinheiro=650

if clima=="sol" or (dinheiro>=300 and dinheiro<=500):
    lugar="clube"
else:
    lugar="cinema"

print("\nvou ao "+lugar)
