from math import floor

numero = int(input())

cem = floor(numero/100)
cinquenta = floor((numero%100)/50)
vinte = floor((numero%50)/20)
dez = floor((numero%20)/10)
cinco = floor((numero%10)/5)
um = floor(numero%5)
print(f"{cem} nota(s) de 100\n{cinquenta} nota(s) de 50\n{vinte} nota(s) de 20\n{dez} nota(s) de 10\n{cinco} nota(s) de 5\n{um} moeda(s) de 1")