import random

computer_guess_normal = random.randint(1,100) # easy level
computer_guess_hard = random.randint(1,500)   # hard level

def main():
    while True:
        show_menu()
        choice = int(input("enter choice: "))
        if choice == 2:
            # print(computer_guess_hard)
            user_guess = int(input("enter your guess: "))
            if user_guess > computer_guess_hard:
                print("high")
            elif user_guess < computer_guess_hard:
                print("low")
            elif user_guess == computer_guess_hard:
                print(f"correct guess, your guess:{user_guess} | computer guess:{computer_guess_hard}")
        else:
            # print(computer_guess_normal)
            user_guess = int(input("enter your guess: "))
            if user_guess > computer_guess_normal:
                print("high")
            elif user_guess < computer_guess_normal:
                print("low")
            elif user_guess == computer_guess_normal:
                print(f"correct guess, your guess:{user_guess} | computer guess:{computer_guess_normal}")

            
def show_menu():
    print("1. easy")
    print("2. difficult")

main()