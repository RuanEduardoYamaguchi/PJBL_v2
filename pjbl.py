from fun import *

dificuldade = escolher_dificuldade() #pega a dificuldade da pasta fun

labirinto, maxTesouros = criar_mapa(dificuldade)

# ESTADO INICIAL DO JOGADOR

linha_jogador = 1
coluna_jogador = 1
labirinto[linha_jogador][coluna_jogador] = 'J'

# ESTATÍSTICAS E PONTUAÇÃO
pontuacao = 0
tesourosEncontrados = 0

while True:

    exibir_mapa(labirinto)

    direcao = input('W A S D: ').lower()

    nova_linha = linha_jogador
    nova_coluna = coluna_jogador

    if direcao == 'w':
        nova_linha -= 1

    elif direcao == 's':
        nova_linha += 1

    elif direcao == 'a':
        nova_coluna -= 1

    elif direcao == 'd':
        nova_coluna += 1

    if labirinto[nova_linha][nova_coluna] != '#':
        
        pontuacao -= 5

        if labirinto[nova_linha][nova_coluna] == 'A':

            pontuacao -= 25

        labirinto[linha_jogador][coluna_jogador] = '.'

        linha_jogador = nova_linha
        coluna_jogador = nova_coluna

        if labirinto[linha_jogador][coluna_jogador] == 'T':
            tesourosEncontrados += 1
            pontuacao += 100
            if maxTesouros == tesourosEncontrados:
                print("Você venceu!")
                print("Pontuação:", pontuacao)
                break
                
        labirinto[linha_jogador][coluna_jogador] = 'J'

    else:
        print ("Movimento inválido") #Se a nova posição for uma '#'