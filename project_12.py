import random
print("Welcome to the Game of Rock Paper Scissors")
while True:
    userChoice = input("Pick your choice: ")
    userChoice = userChoice.lower()

    computerChoice = random.choice(['rock', 'paper', 'scissors'])
    if userChoice == "forfeit":
        break
    
    print(f"Computer chose {computerChoice}")
    

    if userChoice == computerChoice:
        print("You tied")
        continue;
    elif userChoice == "paper" and computerChoice == "rock":
        print("You won, well played!")
        break;
    elif userChoice == "rock" and computerChoice == "scissors":
        print("You won, well played!")
        break;
    elif userChoice == "scissors" and computerChoice == "paper":
        print("You won, well played!")
        break;
    else:
        print("GG! you lost. Try again or maybe Forfeit")
        

