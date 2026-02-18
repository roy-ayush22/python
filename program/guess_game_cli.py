import random

def main():    
    show_menu()
    choice = int(input("enter choice: "))
    if choice == 2:
        hard_mode()
    else:
        easy_mode()

def show_menu():
    print("1. easy")
    print("2. difficult")

def return_menu():
    print("1. play again")
    print("2. exit")
    return_choice = int(input("enter choice: "))
    if return_choice == 1:
        main()  # restart the game
    else:
        print("thanks for playing, goodbye!")

def hard_mode(): 
    computer_guess_hard = random.randint(1, 500)
    while True:
        user_guess = int(input("enter your guess: "))
        if user_guess > computer_guess_hard:
            print("high")
        elif user_guess < computer_guess_hard:
            print("low")
        elif user_guess == computer_guess_hard:
            print(f"correct guess, your guess:{user_guess} | computer guess:{computer_guess_hard}")
            return_menu()
            return

def easy_mode():
    computer_guess_normal = random.randint(1, 100)
    while True:
        user_guess = int(input("enter your guess: "))
        if user_guess > computer_guess_normal:
            print("high")
        elif user_guess < computer_guess_normal:
            print("low")
        elif user_guess == computer_guess_normal:
            print(f"correct guess, your guess:{user_guess} | computer guess:{computer_guess_normal}")
            return_menu()
            return

main()