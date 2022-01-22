import random

def play():
    user = input(f"'r' for Rock, 'p' for paper, 's' for Scisors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'it\'s a tie'
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'you lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())