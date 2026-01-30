from pokemon import Pokemon
from pokedle import game_solo, game_ia, game_1v1, game_1via

def main():

    new_game = input("Do you want play ? [solo/1v1/1via/ia/stop] ")

    while(new_game != "stop"):

        if ( new_game == "solo" ) :
            game_solo()
            
        if ( new_game == "ia" ) :
            game_ia()

        if ( new_game == "1v1" ) :
            game_1v1()

        if ( new_game == "1via" ) :
            game_1via()

        new_game = input("Do you want play again ? [solo/1v1/1via/ia/stop] ")
        
    print("Bye bye !")
    
main()