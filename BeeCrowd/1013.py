a = int(input())
b = int(input())
c = int(input())

valor = (a+b+abs(a-b))/2

if(valor>c):
     print(valor)
else:
    print(f"{c} eh o maior")