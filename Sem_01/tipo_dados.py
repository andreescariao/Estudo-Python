#Tipos de dados
x=1 #int
x="André" #string
x=15.6 #float
x=true #bool

#numero complexo
n1=5;n2=2;x=complex(n1,n2) 
print(x.real)
print(x.imag)

#print("valor: "+str(x))
print("tipo: "+str(type(x)))

#arrais e listas / OBS: Valores podem ser alterados
x=["carro","aviao","navio"] 
print("valor: "x[0])

#Tuplas / OBS: Valores não podem ser alterados
x=("carro","aviao","navio") 

#metodo rang para lista
x=range(0,100)

#Dict
x={
    "Nome":"Andre",
    "Curso":"Engenharia Elétrica"
}
print("Valor: "x["nome"])
