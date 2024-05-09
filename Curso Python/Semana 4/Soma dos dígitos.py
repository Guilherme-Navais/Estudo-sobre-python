numero = int(input("Digite um número inteiro: "))
num_escrito = str(numero)
contador = 0
soma = 0
numero_soma = 0

while contador <= len(num_escrito):
    numero_soma = numero % 10
    soma = soma + numero_soma
    numero = numero // 10
    contador = contador + 1 


print(soma)