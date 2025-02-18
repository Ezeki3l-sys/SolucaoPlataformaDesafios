entrada = input().split()
print(type(entrada))
valor = float(entrada[2])
quantia = int(entrada[1])
preco = valor*quantia
print(f"VALOR A PAGAR: R$ {preco:.2f}")