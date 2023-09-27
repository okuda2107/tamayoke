from game import *

def main():
    my_game = game()
    success: bool = my_game.initialize()
    if success:
        my_game.run_loop()
    
    my_game.shutdown()

main()