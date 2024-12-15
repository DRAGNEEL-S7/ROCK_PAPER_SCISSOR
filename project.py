import random

options= ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper, or scissors: ")
x=user_choice.lower()

computer_choice = random.choice(options)
print("Computer chose:",computer_choice)

if x == computer_choice:
    print("It's a tie!")
    
elif (x == "rock" and computer_choice == "scissors"):
    print("Congratulations,You win.")
    
elif (x == "scissors" and computer_choice == "paper"):
    print("Congratulations,You win.")
    
elif (x == "paper" and computer_choice == "rock"):
    print("Congratulations,You win.")
    
else:
    print("Computer wins!")
