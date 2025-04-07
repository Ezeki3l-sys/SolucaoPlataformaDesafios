from random import randrange
numeros = set()
numero = -1

for n in range(1, 101):
    numero =  randrange(1,1000) #int(input())
    print(n)
    if numero>0:
        numeros.add(numero)

numerosLista = list(numeros)
maior = max(numerosLista)
print(maior)
print(numerosLista.index(maior)+1)
