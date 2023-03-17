import random

def jogar():
    print("*********************************")
    print("Bem vindo ao  jogo de adivinhação")
    print("*********************************")

    total_tentativas = 0
    rodada = 1
    pontos = 1000

    print("qual nivel voce desejar?",
          "0 - facil ",
          "1 - medio",
          "2 - dificl",
          sep='\n'
          )

    selecione_opcao = int(input())

    if(selecione_opcao == 0):
        total_tentativas  = 50
    elif(selecione_opcao == 1):
        total_tentativas = 25
    elif(selecione_opcao == 2):
        total_tentativas = 3
    else:
        total_tentativas = 50

    numero_sorteado = random.randrange(1, 101)

    print(numero_sorteado)
    for rodada in range(1,total_tentativas+1 ):
        print("total: ",pontos)
        print("tentativa {} de {}".format(rodada,total_tentativas))
        chute_str = input("Digite o seu numero no console: ")
        chute = int(chute_str)

        acertou = numero_sorteado == chute
        numero_maior = chute> numero_sorteado
        numero_menor = chute<numero_sorteado


        if(chute <1 or chute >100):
            print("voce digitou um valor incorreto: {}".format(chute))
            continue

        if(acertou):
                print("parabens!, voce acertou e fez {}".format(pontos))
                break
        else:
                if(numero_maior):
                        print("error! numero  maior ")
                elif(numero_menor):
                    print("erro!,numero  menor")
                    pontos_perdidos = abs(numero_sorteado - chute)
                    pontos -= pontos_perdidos



    print("fim do jogo!")

if (__name__ == "__main__"):
        jogar()
