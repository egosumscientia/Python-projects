import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Too low")
        elif guess > random_number:
            print("too high")
    print(f"You've got the number: {random_number} !!!") 

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":

        if low != high:
            guess = random.randiint(low, high)
        else:
            guess = low #could also be high b/c low = high

        feedback = input(f"is {guess} too high (H), too low (L), or correct (C) ???").lower()
        
        if feedback == "h":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1
    
    print(f"Yes! you are correct with the {guess} number")


guess(10)