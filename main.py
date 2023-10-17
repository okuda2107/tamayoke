import traceback
from game import *

def main():
    my_game = Game()
    success: bool = my_game.initialize()
    if success:
        my_game.run_loop()
    
    my_game.shutdown()

try:
    main()
except Exception as e:
    print(traceback.format_exc())