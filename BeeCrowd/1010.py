primeira_peca = input().split()
segunda_pec = input().split()
valor1 = float(primeira_peca[2])
quantia1 = int(primeira_peca[1])
valor2 = float(segunda_pec[2])
quantia2 = int(segunda_pec[1])
preco = valor1*quantia1+valor2*quantia2
print(f"VALOR A PAGAR: R$ {preco:.2f}")