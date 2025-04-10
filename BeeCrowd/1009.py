nome = str(input())
fixo = round(float(input()),2)
vendas = round(float(input()),2)

total = fixo + vendas*0.15

print(f"TOTAL = R$ {total:.2f}")