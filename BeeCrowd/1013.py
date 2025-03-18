a, b, c = (input().split())
a = int(a)
b = int(b)
c = int(c)

valor = (a+b+abs(a-b))//2

if(valor>c):
     print(valor)
else:
    print(f"{c} eh o maior")