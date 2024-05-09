import math

x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

calculo = (x1 - x2)**2 + (y1 - y2)**2
distancia = math.sqrt(calculo)

if distancia >= 10:
    print("longe")
else:
    print("perto")