import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors):")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "its a tie! "
    elif player == "rock":
        if computer == "scissors":
            print("rock smashes scissors, You Win:)!")
        else:
            print("paper covers rock, You Lose:(!")
    elif player == "paper":
        if computer == "rock":
            print("paper covers rock, You Win!")
        else:
            print("scissors cuts paper, You Lose!")
    elif player == "scissors":
        if computer == "paper":
            print("scissors cuts paper, You Win!")
        else:
            print("rock smashes scissors, You Lose!")

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)