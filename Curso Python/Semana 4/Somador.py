vezes = int(input("Digite a quantidade de valores que serão somados: "))
contador = 0
soma = 0

while contador < vezes:
    num = float(input("Digite um número: "))
    soma = soma + num
    contador = contador+1

print("----------------------------------------------------------------------------------")
print("A soma dos números digitados é",soma)