import random
from time import sleep

print("=" * 25)
print("Sortear um número inteiro")
print("=" * 25)
minimo = int(input("Qual é o valor mínimo a sortear? "))
maximo = int(input("Qual é o valor máximo a sortear? "))

escolha = random.randint(minimo, maximo)
sleep(1)

print("O número sorteado foi {}.".format(escolha))
