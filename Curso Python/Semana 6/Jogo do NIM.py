def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n%(m+1) == 0:
        print("\nVocê começa!")
        while n != 0:
            peças_tiradas = usuario_escolhe_jogada(n, m)
            peças_restantes = n - peças_tiradas
            n = peças_restantes
        
            if peças_tiradas == 1:
                print("\nVocê tirou uma peça.")
                print("Agora restam",peças_restantes,"peças no tabuleiro.")

            else:
                print("\nVocê tirou",peças_tiradas,"peças.")
                print("Agora restam",peças_restantes,"peças no tabuleiro.")
            
            if n == 0:
                print("\nFim do jogo! Você ganhou!")
                return 2
            
            else:
                peças_tiradas = computador_escolhe_jogada(n, m)
                peças_restantes = n - peças_tiradas
                n = peças_restantes
        
                if peças_tiradas == 1:
                    print("\nComputador tirou uma peça.")
                    print("Agora restam",peças_restantes,"peças no tabuleiro.")

                else:
                    print("\nComputador tirou",peças_tiradas,"peças.")
                    print("Agora restam",peças_restantes,"peças no tabuleiro.")

                if n == 0:
                    print("\nFim do jogo! Computador ganhou!")
                    return 1

            
    else:
        print("\nComputador começa!")
        while n != 0 or jogo_termina == True:
            peças_tiradas = computador_escolhe_jogada(n, m)
            peças_restantes = n - peças_tiradas
            n = peças_restantes
    
            if peças_tiradas == 1:
                print("\nComputador tirou uma peça.")
                print("Agora restam",peças_restantes,"peças no tabuleiro.")

            else:
                print("\nComputador tirou",peças_tiradas,"peças.")
                print("Agora restam",peças_restantes,"peças no tabuleiro.")
            
            if n == 0:
                print("\nFim do jogo! O computador ganhou!")
                return 1
            
            else:
                peças_tiradas = usuario_escolhe_jogada(n, m)
                peças_restantes = n - peças_tiradas
                n = peças_restantes
        
                if peças_tiradas == 1:
                    print("\nVocê tirou uma peça.")
                    print("Agora restam",peças_restantes,"peças no tabuleiro.")

                else:
                    print("\nVocê tirou",peças_tiradas,"peças.")
                    print("Agora restam",peças_restantes,"peças no tabuleiro.")

                if n == 0:
                    print("\nFim do jogo! Você ganhou!")
                    jogo_termina = True
                    return 2

def usuario_escolhe_jogada(n, m):
    peças_tiradas = int(input("\nQuantas peças você vai tirar? "))

    if peças_tiradas > m or peças_tiradas > n or peças_tiradas <= 0:
        while peças_tiradas > m or peças_tiradas > n or peças_tiradas <= 0:
            print("\nOops! Jogada inválida! Tente de novo.")
            peças_tiradas = int(input("\nQuantas peças você vai tirar? "))
    
    return peças_tiradas


def computador_escolhe_jogada(n, m):
    valor_maximo = m
    valor_maximo_original = m
    tamanho_original = n
    peças_tiradas = m
    n = n - peças_tiradas
    tamanho_ideal = n%(valor_maximo_original+1)
    
    if tamanho_ideal != 0:
        while  tamanho_ideal != 0:
            m = m -1
            peças_tiradas = m
            n = tamanho_original
            n = n - peças_tiradas
            tamanho_ideal = n%(valor_maximo_original+1)

            if tamanho_ideal == 0:
                return peças_tiradas
            
            elif m <= 1:
                return valor_maximo
    
    else:
        return peças_tiradas


def campeonato():
    computador = 0
    jogador = 0

    print("\n**** Rodada 1 ****\n")
    resultado = partida()
    if resultado == 1:
        computador = computador + 1
    else:
        jogador = jogador + 1
    
    print("\n**** Rodada 2 ****\n")
    resultado = partida()
    if resultado == 1:
        computador = computador + 1
    else:
        jogador = jogador + 1

    print("\n**** Rodada 3 ****\n")
    resultado = partida()
    if resultado == 1:
        computador = computador + 1
    else:
        jogador = jogador + 1

    print("\nPlacar: Você",jogador,"X",computador,"Computador")



print("Bem-vindo ao jogo do NIM! Escolha:")
print("\n1 - para jogar uma partida isolada")
escolhe_modo = int(input("2 - para jogar um campeonato "))
loopping = True

while loopping == True:
    if escolhe_modo == 1:
        partida()
        break
    elif escolhe_modo == 2:
        campeonato()
        break
    else:
        escolhe_modo = int(input("Digite uma opção válida: "))

