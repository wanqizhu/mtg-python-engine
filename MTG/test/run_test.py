from test_player import TestPlayer
from test_game import *
if __name__ == "__main__":
    player1 = TestPlayer(build_land_deck())
    player2 = TestPlayer(build_land_deck())
    test_game = game.Game((player1, player2))
    test_game.play()