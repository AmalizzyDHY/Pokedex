from pokemon import Pokemon
from pokedle import game_solo, game_ia

def main():

    new_game = input("Do you want play ? [solo/ia/stop] ")

    while(new_game != "stop"):

        if ( new_game == "solo" ) :
            game_solo()
            
        if ( new_game == "ia" ) :
            game_ia()

        new_game = input("Do you want play again ? [solo/ia/stop] ")
        
    
main()