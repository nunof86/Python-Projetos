import time
def mad_lips():

    adjective = str(input("Tell me an adjective:"))
    nationality = str(input("Tell me a nationality:"))
    person_name = str(input("Tell me a person name:")).capitalize()
    noun = str(input("Tell me a noun:"))
    adjective2 = str(input("Tell me an adjective:"))
    noun2 = str(input("Tell me a noun:"))
    adjective3 = str(input("Tell me an adjective:"))
    adjective4 = str(input("Tell me an adjective:"))
    plurarl_noun = str(input("Tell me a plurarl noun:"))
    noun = str(input("Tell me a noun:"))
    number = str(input("Tell me a number:"))
    shape = str(input("Tell me a shape:"))
    food = str(input("Tell me a food:"))
    food2 = str(input("Tell me a food:"))
    number2 = str(input("Tell me a number:"))

    time.sleep(2)
    print("Pizza was invented by a {} {} chef named {}.".format(adjective, nationality, person_name))
    print("To make a pizza, you need to take a limp of {}, and make a thin, round {} {}.".format(noun, adjective2, noun2))
    print("Then you cover it with {} sauce, {} cheese, and fresh chopped {}.".format(adjective3, adjective4, plurarl_noun))
    print("Next you have to bake it in a very hot {}.".format(noun2))
    print("When it is done, cut it into {} {}.".format(number, shape))
    print("Some kids like {} pizza the best, but my favorite is the {} pizza.".format(food, food2))
    print("If I could, I would eat pizza {} times a day!".format(number2))

mad_lips()
time.sleep(1)
cont = str(input("Do you want to do it again? (Y/N) ")).capitalize()
while cont == "Y":
    time.sleep(1)
    mad_lips()
    cont = str(input("Do you want to do it again? (Y/N) ")).capitalize()
if cont == "N":
    time.sleep(1)
    print("Mad lips finish.")
else:
    time.sleep(1)
    print("Option invalid.")
