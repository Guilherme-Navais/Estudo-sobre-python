def éPrimo(num):
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
        return False
    else:
        return True


n = int(input("Digite um número inteiro: "))

while n > 0:
    if éPrimo(n):
        print(n, "é primo!")
    else:
        print(n, "não é primo")
    n = int(input("\nDigite um número inteiro: "))

print("\nEncerrando programa...")

