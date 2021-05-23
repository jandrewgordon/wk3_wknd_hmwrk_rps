import unittest
from models.player import Player
from models.game import *

class TestRockPaperScissors(unittest.TestCase):

    def test_player1_rock_player2_scissors_returns_player_1_win(self):
        player1 = Player("Andrew", "rock")
        player2 = Player("David", "scissors")
        self.assertEqual(player1, decide_result(player1, player2))

    def test_player1_paper_player2_paper_return_draw(self):
        player1 = Player("Calum", "paper")
        player2 = Player("Saad", "paper")
        self.assertEqual(None, decide_result(player1, player2))