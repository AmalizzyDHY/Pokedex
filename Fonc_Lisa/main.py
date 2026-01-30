from pokemon import Pokemon
from pokedle import game

def main():

    new_game = input("Do you want play ? [y/n/stop] ")

    while(new_game != "stop"):
        new_game = input("Do you want play again ? [y/n/stop] ")

        if ( new_game == "y" ) :
            game()
    
main()