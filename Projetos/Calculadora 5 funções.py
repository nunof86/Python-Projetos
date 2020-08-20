from time import sleep

def soma(x, y):
    return x + y

def menos(x, y):
    return x - y

def multi(x, y):
    return x * y

def divi(x, y):
    return x / y

def pote(x, y):
    return x ** y

def contas():
    escolha = int(input("Escolha uma opção: "))
    if escolha in (1, 2, 3, 4, 5):
        num1 = float(input("Pimeiro número: "))
        num2 = float(input("Segundo número: "))
        sleep(1)

        if escolha == 1:
            print("A soma de {} com {} é {}.".format(num1, num2, soma(num1, num2)))
        elif escolha == 2:
            print("A subtração de {} com {} é {}.".format(num1, num2, menos(num1, num2)))
        elif escolha == 3:
            print("A multiplicação de {} com {} é {}.".format(num1, num2, multi(num1, num2)))
        elif escolha == 4:
            print("A divisão de {} com {} é {}.".format(num1, num2, divi(num1, num2)))
        elif escolha == 5:
            print("A potência de base {} com expoente {} é {}.".format(num1, num2, pote(num1, num2)))
    else:
        print("Opção inválida.")

print("=" * 11)
print("Calculadora")
print("=" * 11)
print("""
[ 1 ] Soma
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão
[ 5 ] Potência""")

contas()
continuar = str(input("Deseja continuar? (S/N): ")).capitalize()
while continuar == "S":
    contas()
    continuar = str(input("Deseja continuar? (S/N): ")).capitalize()
if continuar == "N":
    print("Cálculos terminados.")
else:
    print("Opção onválida.")
    while continuar != "S" != "N":
        print("Opção inválida.")
        continuar = str(input("Deseja continuar? (S/N): ")).capitalize()
        if continuar == "S":
            contas()
        elif continuar == "N":
            print("Cálculos terminados.")
