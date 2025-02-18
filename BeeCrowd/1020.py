from math import floor
d = int(input())
anos = floor(d/365)
meses = floor((d%365)/30)
dias = floor((d%365)%30)

print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")