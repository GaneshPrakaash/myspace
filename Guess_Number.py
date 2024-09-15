# import art
import random
logo = """
  _   _                 _                  _____                     
 | \ | |               | |                / ____|                    
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __|
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/
"""

# TODO: Generating a random number to Guess
SECRET_NUMBER = random.randint(1, 101)
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


# TODO: Defining a function to check the Guess Number
def guess_number(guess):
    """This function will check if the Guessed Number is correct"""
    if guess == SECRET_NUMBER:
        return f"You got it! The answer was {SECRET_NUMBER}."
    elif guess > SECRET_NUMBER:
        return "Too High."
    elif guess < SECRET_NUMBER:
        return "Too Low."


# TODO: Creating a function to Loop through the attempts based on level
def game_on(no_attempt):
    """This function will provide the User with the number of attempts based on difficulty level"""
    while no_attempt > 0:
        print(f"You have {no_attempt} attempts remaining to guess the number.")
        try:
            guess_num = (int(input("Make a guess: ")))
        except ValueError:
            print("Please enter a valid integer between 1 to 100")
            guess_num = (int(input("Make a guess: ")))
        if guess_num in range(1, 101):
            print(guess_number(guess_num))
            if guess_num == SECRET_NUMBER:
                break
            else:
                no_attempt -= 1
                if no_attempt != 0:
                    print("Guess again.")
            if no_attempt == 0:
                print("You've run out of guesses, you lose.")
        else:
            print("Please enter a valid number between 1 to 100")


# print(art.logo)
print(logo)
print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")

# TODO: Obtain the difficulty level from the User
play = True
while play:
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "hard":
        play = False
        game_on(HARD_ATTEMPTS)
    elif level == "easy":
        play = False
        game_on(EASY_ATTEMPTS)
    else:
        print("please enter a valid input")


   
