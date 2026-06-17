def escolher_dificuldade():
                                   #Laço de repetição para garantir que o usuário só vai sair dessa tela CASO escolha uma dificuldade válida
    print('Escolha o modo do jogo')
    print('1 - Fácil')
    print('2 - Normal')
    print('3 - Difícil')

    opcao = int(input('Digite 1, 2 ou 3: '))

    if opcao == 1:
        return 'facil'
            
    elif opcao == 2:
        return 'normal'
            
    elif opcao == 3:
        return 'dificil'
            
    else:
        print('Opção inválida! Tente novamente.\n')
    


def criar_mapa(dificuldade):
    if dificuldade == 'facil':
        labirinto = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '#', '.', '#', '.', '#', '.', '.', '#'],
            ['#', '.', '#', '.', '.', '.', '.', '#', '.', '#'],
            ['#', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
            ['#', '.', '#', '.', '.', '.', '#', '.', 'A', '#'],
            ['#', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
            ['#', '.', '#', '.', '.', '.', '#', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', 'T', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ]
        maxTesouros = 1

    elif dificuldade == 'normal':
        labirinto = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '.', 'A', '#', '.', '.', '.', '#', '.', '#'],
            ['#', '.', '#', '.', '#', '.', '#', '.', '.', '#'],
            ['#', '.', '#', '.', '.', 'A', '.', '#', '.', '#'],
            ['#', '.', '#', '#', '#', '#', '.', '#', '.', '#'],
            ['#', '.', '.', '.', 'T', '#', '.', '.', '.', '#'],
            ['#', '#', '#', '.', '#', '#', '.', '#', '#', '#'],
            ['#', '.', 'A', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '#', '#', '#', 'A', '#', '#', '.', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', 'T', '#'],
        ]
        maxTesouros = 2

    elif dificuldade == 'dificil':
        labirinto = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '#', '.', '#', '.', '#', '.', '.', '#'],
            ['#', '.', '#', '.', '#', 'A', '#', '#', '.', '#'],
            ['#', '.', '#', '.', '.', '.', '.', '#', '.', '#'],
            ['#', '.', '#', '#', '#', '#', 'A', '#', '.', '#'],
            ['#', '.', '.', '.', 'A', 'T', '.', '.', '.', '#'],
            ['#', '#', '#', '.', '#', '#', '.', '#', '#', '#'],
            ['#', 'A', '.', '.', '.', '.', '.', '.', 'A', '#'],
            ['#', 'T', '#', '#', '#', '.', '#', '#', '.', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', 'T', '#'],
        ]
        maxTesouros = 3

    return labirinto, maxTesouros


def exibir_mapa(labirinto):
    for linha in labirinto:  # pega cada linha da matriz
        for celula in linha:  # pega cada célula da linha
            print(celula, end=' ')  # imprime na mesma linha
        print()  # pula pra próxima linha