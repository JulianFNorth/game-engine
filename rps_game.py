from dataclasses import dataclass, field
import random

@dataclass
class GameEngine:
    moves: list = field(default_factory=lambda: ["rock", "paper", "scissors"], init=False)
    
    def get_computer_move(self):
        choice = random.randint(0,2)
        return self.moves[choice]
    
    def decide_winner(self, player_move:str, computer_move:str):
        if player_move == computer_move:
            return "Tie"
        elif player_move == "rock":
            if computer_move == "paper":
                return "Lose"
            return "Win"
        elif player_move == "paper":
            if computer_move == "scissors":
                return "Lose"
            return "Win"
        elif player_move == "scissors":
            if computer_move == "rock":
                return "Lose"
            return "Win"
    
def get_player_move():
    player_move = ""
    while player_move not in ["rock", "paper", "scissors"]:
        player_move = input("What is your move (rock, paper, or scissors)? ").lower().strip()
        if player_move not in ["rock", "paper", "scissors"]:
            print("Please enter a valid choice!\n")
    return player_move

def main():
    game = GameEngine()
    player_move = get_player_move()
    computer_move = game.get_computer_move()
    winner = game.decide_winner(player_move, computer_move)
    print(f"Player move: {player_move}")
    print(f"Computer move: {computer_move}")
    print(f"The winner is {winner}!")

if __name__ == "__main__":
    main()