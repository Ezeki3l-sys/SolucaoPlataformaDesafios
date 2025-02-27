# cpf = str(input("Digite o CPF: "))
valido = str(input("Digite um CPF corretamente: \n"))
verdadeiro = []

for n in valido:
    if n in "0123456789":
        valor = int(n)
        verdadeiro.append(valor) 

resto_1 = (10*verdadeiro[0]+9*verdadeiro[1]+8*verdadeiro[2]+7*verdadeiro[3]+6*verdadeiro[4]+5*verdadeiro[5]+4*verdadeiro[6]+3*verdadeiro[7]+2*verdadeiro[8])%11

if (resto_1<2):
    digito1 = 0
else:
    digito1 = 11-resto_1

resto_2 = (11*verdadeiro[0]+10*verdadeiro[1]+9*verdadeiro[2]+8*verdadeiro[3]+7*verdadeiro[4]+6*verdadeiro[5]+5*verdadeiro[6]+4*verdadeiro[7]+3*verdadeiro[8]+2*verdadeiro[9])%11

if (resto_2<2):
    digito2 = 0
else:
    digito2 = 11-resto_2

if (verdadeiro[-2] != digito1 and verdadeiro[-1] != digito2):
    print("CPF inválido! \n")
else:
    print("CPF válido! \n")