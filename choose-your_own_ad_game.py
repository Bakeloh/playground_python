name = input("Type your name")
print("Welcome", name, "to this adventure!")

answer = input(
    "Yoy are on a dirt road, it has come to an end you can go left or right? Which way would you like to go " 
    
).lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk and swim to swim accross: ? ")
    
    if answer == "swim":
        print("You swam acrross and was eaten by a crocodile. ")
        
elif answer == "walk":
    print("You walked in the forest and was eated by a lion. ")    

elif answer  == "right":
    answer = input("You've come to a bridge, it looks week do you want to cross it or walk back (cross/back)? ")

    if answer == "back":
        print("You can go back and lose. ")
        
elif answer == "cross":
    print("You cross and find a house. Do you go inside it? . ")   
    
    if answer == "yes":
       print ("There is a treasure chest with gold coins.")  
        
    
    elif answer == "no":
      print("The door opens and there is a dragon guarding it. What do you do? \n" +
            "\t1) Attack the dragon.\n" +
            "\t2) Try to negotiate with the dragon.\n" )
#  Add option for you win or die  
d_or_a=input("What will you do?\n")

if d_or_a=="attack":
    print("You attacked the dragon and won.")
else:
    print("You tried to negotiate with the dragon and died.")

    
else:
    print("Invalid response please try again.")
    