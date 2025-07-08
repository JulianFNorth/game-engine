from dataclasses import dataclass, field
import random, time, os
import yaml
from pathlib import Path

STATS_FILE = Path("stats.yaml")

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
    
def load_games(STATS_FILE):
    if STATS_FILE.exists():
        with open(STATS_FILE, "r") as file:
            data = yaml.safe_load(file)
            return data if data is not None else {"wins": 0, "losses": 0, "ties": 0}
    return {"wins": 0, "losses": 0, "ties": 0}

def save_games(STATS_FILE, stats):
    with open(STATS_FILE, "w") as file:
        yaml.safe_dump(stats, file)

def get_player_move():
    player_move = ""
    while player_move not in ["rock", "paper", "scissors"]:
        player_move = input("What is your move (rock, paper, or scissors)? ").lower().strip()
        if player_move not in ["rock", "paper", "scissors"]:
            print("Please enter a valid choice!\n")
    return player_move

def scoring(winner, human_score, computer_score):
    if winner == "Win":
        human_score += 1
    elif winner == "Lose":
        computer_score += 1
    return human_score, computer_score

def get_games():
    games = ""
    while games not in ['3', '5']:
        games = input("How many best-of games would you like (3 or 5)? ")
        if games not in ['3','5']:
            print("Please enter 3 or 5!\n")

    if games == '3':
        return 3
    return 5

def main():
    games = get_games()
    counter = games
    human_score = 0
    computer_score = 0
    stats = load_games(STATS_FILE)

    while games:
        game = GameEngine()
        player_move = get_player_move()
        computer_move = game.get_computer_move()
        winner = game.decide_winner(player_move, computer_move)
        human_score, computer_score = scoring(winner, human_score, computer_score)

        print(f"Player move: {player_move}")
        time.sleep(0.5)
        print(f"Computer move: {computer_move}")
        time.sleep(1)
        print(f"The winner is the {'player' if winner == 'Win' else ('none' if winner == 'Tie' else 'computer')}!")
        games -= 1
    
        time.sleep(1)
        print(f"\nThe result is:\nHuman score: {human_score}.\nComputer score: {computer_score}.")
        time.sleep(2)
        os.system('clear')
    
    stats["wins"] += human_score
    stats["losses"] += computer_score
    stats["ties"] += counter - (human_score + computer_score)
    save_games(STATS_FILE, stats)

    time.sleep(1)
    print(f"The final winner is the {'player' if human_score > computer_score else ('none' if human_score == computer_score else 'computer')}!")
    print(f"Stats:\nHuman wins: {human_score} Human losses: {computer_score}.\nComputer wins: {computer_score} Computer losses: {human_score}.")
    print(f"\nTotal Stats: {load_games(STATS_FILE)}")

if __name__ == "__main__":
    main()
