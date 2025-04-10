# -*- coding: utf-8 -*-

numero = int(input())
numero2 = numero
cem = numero//100
numero = numero-cem*100
cinquenta = numero//50
numero = numero-cinquenta*50
vinte = numero//20
numero = numero-vinte*20
dez = numero//10
numero = numero-dez*10
cinco = numero//5
numero = numero-cinco*5
dois = numero//2
numero = numero-dois*2
um = numero//1
numero = numero-um
print(numero2)
print(f"{cem} nota(s) de R$ 100,00\n{cinquenta} nota(s) de R$ 50,00\n{vinte} nota(s) de R$ 20,00\n{dez} nota(s) de R$ 10,00\n{cinco} nota(s) de R$ 5,00\n{dois} nota(s) de R$ 2,00\n{um} nota(s) de R$ 1,00")