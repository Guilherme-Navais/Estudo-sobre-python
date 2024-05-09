num = int(input("Digite um número inteiro: "))
numero_igual = False

while num > 0 and not numero_igual:
    ultimo = num % 10
    num = num // 10
    proximo = num % 10
    if ultimo == proximo:
        numero_igual = True

        
if not numero_igual:
    print("não")
else:
    print("sim")
