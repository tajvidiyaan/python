import random 
player1 =random.choice(["Rock" , "Paper" , "Scissors"])
print(player1)
player2 = input("Rock" " or " "Paper" " or " "Scissors ?")
if player1 == "Rock" and player2 == "Rock" or player1 == "Paper" and player2 == "Paper" or player1 == "Scissors" and player2 == "Scissors":
    print("equal")
elif player1 == "Rock" and player2 == "Paper" or player1 == "Paper" and player2 == "Scissors" or player1 == "Scissors" and player2 == "Rock":
    print("you win")
elif player1 == "Paper" and player2 == "Rock" or player1 == "Scissors" and player2 == "Paper" or player1 == "Rock" and player2 == "Scissors":
    print("you lost")
else:
    print("!!!")