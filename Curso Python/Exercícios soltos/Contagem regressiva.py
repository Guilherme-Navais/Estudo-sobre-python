num = int(input("Digite um número inteiro: "))

while num < 0 or type(num) != int:
    print("Digite um número válido")
    num = int(input("\nDigite um número inteiro: "))


def impar_ou_par(n):
    if n%2 == 0:
        return "par"
    else:
        return "ímpar"
    
while num > 0:
    print(num,"é",impar_ou_par(num))
    num = num - 1