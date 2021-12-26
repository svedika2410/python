print("Welcome to the quiz ")
playing = input("Wish to play? ")
if playing != "yes":
    quit()

print("Lets play!")
score =0 

answer = input("Are we humans?  ")
if answer == "yes":
    print("Correct!")
    score += 1
else:
    print("False")
answer = input("Do you study in college?  ")
if answer == "yes":
    print("Correct!")
    score += 1
else:
    print("False")
answer = input("Are you in AI?  ")
if answer == "yes":
    print("Correct!")
    score += 1
else:
    print("False")

print("Your score is:",score,"out of 3")
