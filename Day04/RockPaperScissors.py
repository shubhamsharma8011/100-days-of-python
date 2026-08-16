import random 
print("What do you want to choose?",end="") 
users_choice=int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

rock="""    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
game=[rock,paper,scissors]
print(game[users_choice])

comp_choice=random.randint(0,2)
print("Computer chose: ",game[comp_choice])

if users_choice>=3 or users_choice<=0:
    print("Invalid Number, You Lose!")
elif users_choice==0 and comp_choice==2:
    print("You Win!")
elif users_choice==2 and comp_choice==0:
    print("You Lose!")
elif comp_choice > users_choice:
    print("You Lose!")
elif comp_choice < users_choice:
    print("You Win!")
elif comp_choice==users_choice:
    print("It's a DRAW!")
