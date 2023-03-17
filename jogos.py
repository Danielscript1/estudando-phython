import adivinhaca
import foca

def main():
    print("*********************************")
    print("Bem vindo! escolha o  jogo desejado")
    print("*********************************")

    print("escolha o jogo desejado",
          " 0 - adivinhaca",
          " 1 - foca",
          sep='\n')
    escolha = int(input("aguardando escolha: "))

    if(escolha == 0):
        adivinhaca.jogar()
    elif(escolha ==1):
        foca.jogar()
    else:
        print("escolha um jogo")
        main()
if (__name__ == "__main__"):
        main()