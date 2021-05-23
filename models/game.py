class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

def decide_result(player1, player2):
    
    # Player 1 chooses Rock
    if player1.choice == "rock":
        if player2.choice == "paper":
            return player2
        elif player2.choice == "scissors":
            return player1
        else:
            return None
    
    # Player 1 chooses Paper
    if player1.choice == "paper":
        if player2.choice == "scissors":
            return player2
        elif player2.choice == "rock":
            return player1
        else:
            return None

    # Player 1 chooses Scissors
    if player1.choice == "scissors":
        if player2.choice == "rock":
            return player2
        elif player2.choice == "paper":
            return player1
        else:
            return None

def play_computer(player1):
    computer_move = Random.choice(["rock", "paper", "scissors"])
    print(computer_move)

