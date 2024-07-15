"""Rock , paper, scissors.. Game"""
import random
user_choice=int(input("What do you choose? type 0 for Rock, 1 for paper,2 for Scissors.\n"))
computer_choice= random.randint(0, 2)
print(f"computer_choice {computer_choice}")
if user_choice>=3 or computer_choice<0:
    print("you typed an invalid number, you lose!.")
if user_choice==0 & computer_choice==2:
    print("you winn.")
elif computer_choice ==0 & user_choice ==2:
    print("you win..")
elif computer_choice > user_choice:
    print("you lose..")
elif user_choice > computer_choice:
    print("you win.")
elif computer_choice==user_choice:
    print("it is draw.")
