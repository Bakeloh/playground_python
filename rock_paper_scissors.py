import random

# first we declare our variables
user_wins = 0
computer_wins = 0

# while True:
#     # get user input for rock, paper or scissors
#     user_input = input("Type Rock/Paper/Scissors: ").lower()
    
#     if not (user_input == 'rock' or user_input == 'paper' or user_input == 'scissors'):
#         print('Invalid Input! Please type Rock, Paper or Scissors')
#         continue
        
#     # generate a random number between 1 and 3 to represent the computer's choice
#     computer_random_number = random.randint(1, 4)
#     computer_choice = ['rock', 'paper', 'scissors'][computer_random_number - 1]
    
#     # compare the inputs of the user and the computer
#     if user_input == computer_choice:
#         result = "It's a tie!"
#     elif (user_input == 'rock' and computer_choice == 'scissors') or \
#             (user_input == 'scissors' and computer_choice == 'paper') or \
#             (user_input == 'paper' and computer_choice == 'rock'):
#         user_wins += 1
#         result = f"Congratulations! You win this round. Your score is {user_wins}."
#     else: 
#         computer_wins += 1
#         result = f"Sorry, you lose this round. The computer wins with {computer_choice}. Computer score is {computer_wins}."

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit. ").lower()
    if user_input == 'q':
        break
        
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    
    if user_input == "rock" and computer_pick ==  "scissors":
        print("You win!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick ==  "rock":
        print("You win!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick ==  "paper":
        print("You win!")
        user_wins += 1

    else:   
        print("You lost!")
        computer_wins += 1   
        
print("You won", user_wins, "times. ")                                                   
print("The computer won", computer_wins, "times. ")    
print("Goodbye")    






# import random

# # declare variables to track wins
# user_wins = 0
# computer_wins = 0

# # options for the game
# options = ["rock", "paper", "scissors"]

# while True:
#     user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
#     if user_input == 'q':
#         break
        
#     if user_input not in options:
#         print('Invalid input! Please type Rock, Paper, or Scissors.')
#         continue
    
#     # computer chooses randomly
#     computer_pick = random.choice(options)
#     print("Computer picked", computer_pick + ".")
    
#     # determine the winner
#     if (user_input == "rock" and computer_pick == "scissors") or \
#        (user_input == "paper" and computer_pick == "rock") or \
#        (user_input == "scissors" and computer_pick == "paper"):
#         print("You win!")
#         user_wins += 1
#     elif user_input == computer_pick:
#         print("It's a tie!")
#     else:
#         print("You lost!")
#         computer_wins += 1

# # print final scores
# print("You won", user_wins, "times.")
# print("The computer won", computer_wins, "times.")
# print("Goodbye!")
