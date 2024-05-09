import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
print("-------------------------------------------------------------------------------------")
delta = b**2 - 4*a*c

def duas_raízes_reais():
    raiz = math.sqrt(delta)
    x1 = (-b + raiz) / (2*a)
    x2 = (-b - raiz) / (2*a)
    if x1 > x2:
        print("as raízes da equação são",x2,"e",x1)
    else:
        print("as raízes da equação são",x1,"e",x2)

def uma_raiz_real():
    x1 = (-b) / (2*a)
    print("a raiz desta equação é",x1)

def sem_raízes_reais():
    print("esta equação não possui raízes reais")

if delta > 0:
    duas_raízes_reais()

elif delta == 0:
    uma_raiz_real()

elif delta < 0:
    sem_raízes_reais()
    
else:
    print("Digite valores válidos")
