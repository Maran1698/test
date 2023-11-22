#welcome notes
print("welcome to my quiz game!")
#enter the input
player = input("Do you want to play? ")
#if class for enter qustion -'yes or no'
if player.lower() != "yes":
    quit()

print("Let's start the game :)")
score = 0

answer = input("What does IAS stand for? ")
if answer.lower() == "indian administrative service":
    print("Correct!")
    score += 1
else:
    print("Better luck next time.")

answer = input("What does IPS stand for? ")
if answer.lower() == "indian police service":
    print("Correct!")
    score += 1
else:
    print("Better luck next time.")

answer = input("What does 6 + 9 equal? ")
if int(answer) == 15:
    print("Correct!")
    score += 1
else:
    print("Better luck next time.")

print("Thank you! You got " + str(score) + " questions correct :)")
