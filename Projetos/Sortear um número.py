import random
from time import sleep
minimo = int(input("Qual é o valor mínimo a sortear? "))
maximo = int(input("Qual é o valor máximo a sortear? "))

escolha = random.randint(minimo, maximo)
sleep(1)

print("O número sorteado foi {}.".format(escolha))
