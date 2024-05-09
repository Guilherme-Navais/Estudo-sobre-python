num = int(input("Digite um número inteiro: "))
contador = num
divide = num
primo = True

while divide != 2:
    divide = contador - 1
    contador = contador - 1
    if num % divide == 0:
        divide = 2
        primo = False

if not primo:
    print("não primo")
else:
    print("primo")
