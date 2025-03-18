lista = [5,6,4]
lista2 = [2,4,3]
v1 = ""
v2 = ""
resultado = []

for n in range(len(lista)-1,-1,-1):
    v1 = v1+str(lista[n])
    v2 = v2+str(lista2[n])
v3 = int(v1)+int(v2)
v3 = str(v3)

for n in v3:
    resultado.insert(0,n)
print(resultado)