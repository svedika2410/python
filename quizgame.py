print("Welcome to the quiz ")
playing = input("Wish to play? ")
if playing != "yes":
    quit()

print("Lets play!")
score =1
def checkscore(x):
    if x<0:
        print("Game over")
        print("Exit")
        exit()
    

answer = input("Are we humans?  ")
if answer == "yes":
    print("Correct!")
    score += 1
    checkscore(score)
else:
    print("False")
    score -= 1
    checkscore(score)
answer = input("Do you study in college?  ")
if answer == "yes":
    print("Correct!")
    score += 1
    checkscore(score)
else:
    print("False")
    score -= 1
    checkscore(score)
answer = input("Are you in AI?  ")
if answer == "yes":
    print("Correct!")
    score += 1
    checkscore(score)
else:
    print("False")
    score -= 1
    checkscore(score)

print("Your score is:",score,"out of 3")

    


