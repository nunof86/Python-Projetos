import random
from time import sleep

def sorteio():
    print("=" * 13)
    print("Lança o dado:")
    print("=" * 13)
    escolha = random.randint(1,6)
    sleep(1)

    print("O número sorteado foi {}.".format(escolha))

sorteio()
continuar = str(input("Deseja voltar a sortear? (S/N)")).capitalize()
while continuar == "S":
    sorteio()
    continuar = str(input("Deseja voltar a sortear? (S/N)")).capitalize()
if continuar == "N":
    print("Fim do sorteio.")
else:
    print("Opção inválida.")
