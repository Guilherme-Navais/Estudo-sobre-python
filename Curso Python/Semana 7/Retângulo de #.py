largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
contador = largura

while altura >= 1:
    while contador >= 1:
        print("#", end = '')
        contador = contador - 1
    
    print()
    altura = altura -1
    contador = largura
