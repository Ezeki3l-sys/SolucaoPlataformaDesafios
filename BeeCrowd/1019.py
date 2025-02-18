from math import floor

s = int(input())
segundos = 0
minutos = 0
horas = 0
for n in range(1,s+1):
    segundos = segundos + 1
    if(segundos%60==0):
        minutos = minutos + 1
        segundos = segundos - 60
        if(minutos%60==0):
            horas = horas + 1
            minutos = minutos - 60

print(f"{horas}:{minutos}:{segundos}")
