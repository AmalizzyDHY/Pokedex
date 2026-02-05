from Fonc_Lisa.main import main as l_main
from Fonc_Sam.main import random_matchup, random_team, team_vs_team

def poulpe():
    
    print("\nWelcome ! To Smart Pokedex !\n")
    print("You can :")
    print("(1) - Create a Team")
    print("(2) - Pokemon Battle")
    print("(3) - Team Battle")
    print("(4) - Play pokedle\n")

    choice = input("Which feature would you like to use ? [1/2/3/4/bye] : ")

    while(choice != "bye"):
        if ( choice == "1" ):
            print("Let's go for : Create Team !")
        if ( choice == "2" ):
            print("Let's go for : Matchup !")
            random_matchup()
        if ( choice == "3" ):
            print("Let's go for : Team Battle")
        if ( choice == "4"):
            print("Let's go for : Pokedle !")
            l_main()

        choice = input("Which feature would you like to use ? [1/2/3/4/bye] : ")

    print("Bye bye")

poulpe()