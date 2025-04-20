import random
randnum = random.randint(1,100)
score = 0
while True:
    user = int(input("enter a number (1,100) for playing a game:"))
    score += 1
    if user == randnum:
        print("you exist!")
        break
    elif user > 100:
        print("invalid choice! enter number between (1 to 100)!")
    else:
        if user < randnum:
            print("guese number is too small. try with big number.")
        else:
            print("guese number is too big. try with small number.")

newscore = 100 - score
print("your final score is:",newscore)
try:
    with open("highscore.txt","r") as f:
        hscore = int(f.read())
except FileNotFoundError:
    hscore = 0
if hscore < newscore:
    hscore = newscore
    with open("highscore.txt","w") as f:
        f.write(str(hscore))
print("your highest score is:",hscore)
