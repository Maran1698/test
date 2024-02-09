#---this is quis game 
 #   i have a habite with some to asking any question .i need to find out the answers othewise i am festrating.
  #  so i develope this qeis game 

#your also enjoy it..are you like----


#welcome notes:
print("welcome to my quiz game!")
#enter the input
player = input("Do you want to play? ")
#if class for enter qustion -'yes or no'
if player.lower() != "yes":
    quit()
#inner welcome
print("Let's start the game :)")
score = 0
#1st question
answer = input("What does IAS stand for? ")
# answer correct means score gives 1
if answer.lower() == "indian administrative service":
    print("Correct!")
    score += 1
# answer not correct     
else:
    print("Better luck next time.")
#2nd question
answer = input("What does IPS stand for? ")
# answer correct means score gives 1
if answer.lower() == "indian police service":
    print("Correct!")
    score += 1
# answer not correct 
else:
    print("Better luck next time.")
#3rd question
answer = input("What does 6 + 9 equal? ")
# answer correct means score gives 1
if int(answer) == 15:
    print("Correct!")
    score += 1
# answer not correct 
else:
    print("Better luck next time.")
#4th question
answer = input("What does 30-14 equal? ")
# answer correct means score gives 1
if int(answer) == 16:
    print("Correct!")
    score += 1
# answer not correct 
else:
    print("Better luck next time.")
#5th question
answer = input("What does 10*2 equal? ")
# answer correct means score gives 1
if int(answer) == 20:
    print("Correct!")
    score += 1
# answer not correct 
else:
    print("Better luck next time.")    
#thank u note and add no of score
print("Thank you! You got " + str(score) + " questions correct :)")
