import random
rock = 'r'

paper = 'p'
scissors = 's'
emojis = {rock:"🥌",paper:"📄",scissors:"✂"}
choices = tuple(emojis.keys())

def user_enter():
    while True:
        user_input = input("Enter your choice rock,paper,scissors (r/p/s) ")
        if user_input in choices:
            return user_input
        else:
            print("Invalid!")
def display_choices(user_input,computer_choice):
    print(f"You picked:{emojis[user_input]}")
    print(f"Computer picked:{emojis[computer_choice]}")
def determine_winner(user_input,computer_choice):


        if user_input==computer_choice:
            print(f"You and computer picked the same!")
        elif (
                (user_input== rock and computer_choice== scissors) or
                (user_input== scissors and computer_choice == paper) or
                (user_input== paper and computer_choice == rock)):

            print(f"You won")
        else:
            print(f"Computer won")

def play_game():
    while True:
        computer_choice = random.choice(choices)

        user_input = user_enter()
        display_choices(user_input,computer_choice)
        determine_winner(user_input,computer_choice)
        play_again = input("Do you wanna play again (Y/N) ").upper()
        if play_again=='N':
            break
play_game()
