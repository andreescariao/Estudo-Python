#Tupla 
# Mudar elemento da tupla

t_carros=("HRV","GOLF","ARGO")
l_carros=list(t_carros)
l_carros[2]="FOCUS"
t_carros=tuple(l_carros)

for x in l_carros:
    print(x)
