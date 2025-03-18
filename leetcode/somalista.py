coisas = list((input()).replace(" ", "")) 
coisas2 = list((input()).replace(" ", ""))
fim = []

if (len(coisas)>=len(coisas2)):
    while(len(coisas2)<len(coisas)):
        coisas2.append(0)
    for n in range(0, len(coisas)):
        soma = int(coisas[n])+ int(coisas2[n])
        if(soma>=10):
            soma = soma%10
        fim.append(soma)
else:
    for n in range(0, len(coisas)):
        soma = int(coisas[n])+ int(coisas2[n])
        if(soma>=10):
            soma = soma%10
        fim.append(soma)
print(fim)

