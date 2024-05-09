lista_de_numeros = []

num = int(input("Digite um número: "))

while num != 0:
    lista_de_numeros.append(num)
    num = int(input("Digite um número: "))

tamanho_da_lista = len(lista_de_numeros)
contador = -1

while tamanho_da_lista > 0:
    print(lista_de_numeros[contador])
    contador = contador - 1
    tamanho_da_lista = tamanho_da_lista - 1
