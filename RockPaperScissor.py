import random
print("Let's play Rock Paper Scissor")

options = ["Rock", "Paper", "Scissor"]

n = int(input("Enter number of rounds: "))
user_win = 0
comp_win = 0

for i in range(0,n):
    print(f"Round {i+1}:")
    
    comp = random.choice(options)
    user = input("Enter word by player: ")
    if(user!= "Paper" or "Rock" or "Scissor"):
        print("Invalid input")
    print(f"Computer chose {comp}")
    if(user == "Rock" and comp == "Scissor"):
        print(f"User wins round {i+1}")
        user_win +=1
    elif(user == "Rock" and comp == "Paper"):
        print(f"Computer wins round {i+1}")
        comp_win +=1
    elif(user == "Scissor" and comp == "Paper"):
        print(f"User wins round {i+1}")
        user_win +=1
    elif(user == "Scissor" and comp == "Rock"):
        print(f"Computer wins round {i+1}")
        comp_win +=1
    elif(user == "Paper" and comp == "Rock"):
        print(f"User wins round {i+1}")
        user_win +=1
    elif(user == "Paper" and comp == "Scissor"):
        print(f"Computer wins round {i+1}")
        comp_win +=1
    elif(user == comp):
        print(f"Round {i+1} draw")
    print(f"Scoreboard: \nUser-{user_win} \nComputer-{comp_win}")

print("Game over")
print(f"Final Scoreboard: \nUser-{user_win} \nComputer-{comp_win}")
if(user_win> comp_win):
    print("User wins the game")
elif(user_win< comp_win):
    print("Computer wins")
else:
    print("Game Draw")