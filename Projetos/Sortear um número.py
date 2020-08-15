import random
from time import sleep

def sorteio():
    print("=" * 25)
    print("Sortear um número inteiro")
    print("=" * 25)
    minimo = int(input("Qual é o valor mínimo a sortear? "))
    maximo = int(input("Qual é o valor máximo a sortear? "))

    escolha = random.randint(minimo, maximo)
    sleep(1)

    print("O número sorteado foi {}.".format(escolha))
sorteio()
continuar = str(input("Deseja voltar a sortear? (S/N)")).capitalize()
while continuar == "S":
    sorteio()
    continuar = str(input("Deseja voltar a sortear? (S/N)")).capitalize()
if continuar == "N":
    print("Sorteio terminado.")
else:
    print("Opção inválida.")
