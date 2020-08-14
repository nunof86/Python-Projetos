import random
from time import sleep




def pedra_papel_tesoura():
    print("=" * 20)
    print("Pedra Papel Tesaoura")
    print("=" * 20)
    print("""[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura""")
    escolha = int(input("Escolha uma opção:"))
    lista = ["Pedra", "Papel", "Tesoura"]
    escolha_pc = random.choice(lista)
    if escolha >= 4:
        print("Opção inválida.")
    else:
        print("PEDRA")
        sleep(1)
        print("PAPEL")
        sleep(1)
        print("TESOURA!")
        print("=" * 20)
        print("O computador escolheu {}.".format(escolha_pc))
        if escolha == 1:
            print("O jogador escolheu Pedra.")
        elif escolha == 2:
            print("O jogador escolheu Papel.")
        elif escolha == 3:
            print("O jogador escolheu Tesoura.")
        else:
            print("Escolha inválida.")
        print("=" * 20)
        if escolha_pc == lista[0]:
            if escolha == 1:
                print("Empate!")
            elif escolha == 2:
                print("Ganhou!")
            else:
                print("Perdeu!")
        elif escolha_pc == lista[1]:
            if escolha == 1:
                print("Perdeu!")
            elif escolha == 2:
                print("Empate!")
            else:
                print("Ganhou!")
        elif escolha_pc == lista[2]:
            if escolha == 1:
                print("Ganhou!")
            elif escolha == 2:
                print("Perdeu!")
            else:
                print("Empate!")


pedra_papel_tesoura()
continuar = input("Deseja continuar? (S/N)").capitalize()
while continuar == "S":
    pedra_papel_tesoura()
    continuar = input("Deseja continuar? (S/N)").capitalize()
if continuar == "N":
    print("Jogo terminado.")
else:
    print("Opção inválida.")
