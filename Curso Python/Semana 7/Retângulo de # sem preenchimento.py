largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
altura_original = altura
contador = largura

while altura >= 1:
    if altura == altura_original or altura == 1:
        while contador >= 1:
            print("#", end = '')
            contador = contador - 1
    else:
        while contador >= 1:
            if contador == 1 or contador == largura:
                print("#", end = '')
            else:
                print(" ", end = '')
            contador = contador -1
    
    print()
    altura = altura -1
    contador = largura
