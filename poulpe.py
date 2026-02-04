from Fonc_Lisa.main import main as l_main
from Fonc_Sam.main import main as s_main

def poulpe():
    
    print("Welcome ! To Smart Pokedex !\n")
    print("You can :")
    print("(1) - Create a Team")
    print("(2) - Pokemon Battle")
    print("(3) - Play pokedle\n")
    choice = input("Which feature would you like to use ? [1/2/3/bye] : ")

    while(choice != "bye"):
        if ( choice == "1" ):
            print("let's go for : Create Team !")
        if ( choice == "2" ):
            print("let's go for : Matchup !")
        if ( choice == "3"):
            print("let's go for : Pokedle !")
            l_main()

        choice = input("Which feature would you like to use ? [1/2/3/bye] : ")

    print("Bye bye")

poulpe()