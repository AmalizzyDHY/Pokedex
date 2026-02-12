from .pokedle import game_ia
import matplotlib.pyplot as plt

def graph():
    data = []
    sommes = 0

    for i in range(0, 1000):
        print(i)
        data.append(game_ia())
    print("\n")
    # print(data)

    # Moyenne
    for elem in data:
        sommes += elem
    moyenne = sommes / len(data)
    print("On averagz, AI takes : " + str(moyenne) + " turns to find the mystery Pokemon")

    plt.hist(data, bins=5)
    plt.title("The number of turns the IA needs to find the mystery Pokemon\nOn 1000 attempts")
    plt.xlabel("number of turns")
    plt.ylabel("quantity")
    plt.show()