# cases: of rock
#  rock-rock = tie
#  rock - paper = paper wins
#  rock - scissor = rock wins

#  cases: of paper
#  paper - paper = tie
#  paper - rock = paper wins
#  paper - scissor = scissor wins

#  cases: of scissor
#  scissor - scissor = tie
#  scissor - rock = rock wins
#  scissor -paper = scissor wins

import random
list = ["ROCK", "PAPER", "SCISSOR"]
user_choice = input("ENTER YOUR CHOICE(ROCK, PAPER, SCISSOR) : ").upper()
  
comp_choice = random.choice(list)
print(f"YOUR CHOICE IS {user_choice} AND ROBOT'S CHOICE IS {comp_choice}.")

# NOW WE START DECIDING WHO WINS.
if user_choice == comp_choice:
    print(f"IT'S A DRAW\nBECAUSE YOU CHOOSED {user_choice} AND THE ROBOT ALSO CHOOSE {comp_choice}")
elif user_choice == "ROCK" and comp_choice == "PAPER":
    print("ROBOT WINS")
elif user_choice == "ROCK" and comp_choice == "SCISSOR":
    print("CONGRATS YOU WIN")
elif user_choice == "PAPER" and comp_choice == "SCISSOR":
    print("ROBOT WINS")
elif user_choice == "PAPER" and comp_choice == "ROCK":
    print("CONGRATS YOU WIN")
elif user_choice == "SCISSOR" and comp_choice == "ROCK":
    print("ROBOT WINS")
elif user_choice == "SCISSOR" and comp_choice == "PAPER":      
    print("CONGRATS YOU WIN")
else:
    print("APPEARS THAT YOU ENTERED SOMETHING DIFFERENT THEN WHAT'S MENTIONED")          
