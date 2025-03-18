import math

x1_e_y1 = input().split()
x2_e_y2 = input().split()
x1 = float(x1_e_y1[0])
x2 = float(x2_e_y2[0])
y1 = float(x1_e_y1[1])
y2 = float(x2_e_y2[1])

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"{distancia:.4f}")