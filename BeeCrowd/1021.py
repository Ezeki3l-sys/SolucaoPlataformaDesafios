numero = float(input())

if (0 <= numero <= 1000000.00):
    print("NOTAS: ")
    dinheiros = numero / 100
    print("%d nota(s) de R$ 100.00" % dinheiros)
    numero = numero % 100

    dinheiros = numero / 50
    print("%d nota(s) de R$ 50.00" % dinheiros)
    numero = numero % 50

    dinheiros = numero / 20
    print("%d nota(s) de R$ 20.00" % dinheiros)
    numero = numero % 20

    dinheiros = numero / 10
    print("%d nota(s) de R$ 10.00" % dinheiros)
    numero = numero % 10

    dinheiros = numero / 5
    print("%d nota(s) de R$ 5.00" % dinheiros)
    numero = numero % 5

    dinheiros = numero / 2
    print("%d nota(s) de R$ 2.00" % dinheiros)
    numero = numero % 2

    print("MOEDAS: ")
    moedas = numero / 1.00
    print("%d moeda(s) de R$ 1.00" % moedas)
    numero = numero % 1.00

    moedas = numero / 0.50
    print("%d moeda(s) de R$ 0.50" % moedas)
    numero = numero % 0.50

    moedas = numero / 0.25
    print("%d moeda(s) de R$ 0.25" % moedas)
    numero = numero % 0.25

    moedas = numero / 0.10
    print("%d moeda(s) de R$ 0.10" % moedas)
    numero = numero % 0.10

    moedas = numero / 0.05
    print("%d moeda(s) de R$ 0.05" % moedas)
    numero = numero % 0.05

    moedas = numero / 0.01
    print("%d moeda(s) de R$ 0.01" % moedas)
    numero = numero % 0.01
