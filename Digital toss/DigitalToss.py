import random 
guese = ['head','tail']
win = 0
totalmatches = 0
while True:
    choice = input("Enter head or tail to toss and any key to exit:")
    ranchoice = random.choice(guese)
    if choice == "exit":
        print("you are exit.")
        break
    elif choice not in guese:
        print("enter valid choice.")
        totalmatches -= 1
    else:
        if ranchoice == choice:
            print("you win the game!")
            win += 1
        else:
            print("you lost the game try again.")
    totalmatches += 1
ans = totalmatches / win
winrate = 100 / ans
print("your overall winrate is:",winrate,"%")
with open("highscore.txt","a") as f:
    f.write("\nnew highscore is:")
    f.write(str(winrate))

