from Game import *

def main():
    my_game = Game()
    success: bool = my_game.initialize()
    if success:
        my_game.run_loop()
    
    my_game.shutdown()

main()