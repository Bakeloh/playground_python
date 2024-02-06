
import random

# randrange does not inlude the upperbound while randint does
top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    # above confirms its digit
    top_of_range = int(top_of_range)  # convert string to integer
    
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.  Thank you.")
        quit()

else: 
    print("Please type a number next time.")
    quit()        
    
# r = random.randrange(0,11)
# print(r)

random_number = random.randint(0, top_of_range)   # generate a random integer between 1 and user'
guesses = 0


while True:  # keep looping until correct guess is made
    guesses += 1
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
    # above confirms its digit
        user_guess = int( user_guess)  # convert string to integer
    

    else: 
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it right!") 
        break   
    
    elif user_guess > random_number:
        print("You were above the number!")     
    else:
        print("You were below the number!")
            
    # if guesses >= 6:
    #     print("\nSorry, you used up all your tries.\nThe answer was", random_number)
            
        
        
    print("You got it in", guesses, "guesses")  
    
    
    # check why the above is not working.        



