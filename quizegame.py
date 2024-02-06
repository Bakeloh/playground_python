# Add a try again option  to the game.


print ("Welcome to my computer quize!")

playing = input("Do you want to play? ")
# print (playing)

if playing.lower() != "yes":
# If yes the condition converst to a bollean which is TRUE and whats indented will be run. 
    # if not it will just skip that part of code.
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1   
else:
    print("Incorrect!, CPU stands for Central Processing Unit.")
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!, GPU stands for grapgic processing unit.")
    
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!, RAM stands for random access memory.") 
    
answer = input("What does ROM stand for? ")
if answer.lower() == "random operating memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!, ROM stands for random operating memory.") 
    
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!, PSU power supply unit.")   
    
print("You got " + str(score) + " questions correct!")  
print("You got " + str((score/4) * 100) + "%. ")          

