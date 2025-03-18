valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
pi = 3.14159

print(f"TRIANGULO: {a*(c/2):.3f}\nCIRCULO: {c**2*pi:.3f}\nTRAPEZIO: {(a+b)*c/2:.3f}\nQUADRADO: {b*b:.3f}\nRETANGULO: {a*b:.3f}")
