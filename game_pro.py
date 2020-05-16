import random
a=["rock","paper","scissor"]
print("Welcome to the game ROCK,PAPER,SCISSOR \nIf you want to end the game please type 'QUIT'\nLet us enter into the game ")
while(1) :
   user_choice=(input("Please enter your choice:")).lower()
   comp_choice=random.choice(a)
   if(user_choice!='quit'):
    if (user_choice in a ):
     if(comp_choice==user_choice):
       print("Tie")
       print("The computer choice is " + comp_choice)
     elif((comp_choice=="rock" and user_choice=="paper")or(comp_choice=="paper" and user_choice=="scissor")or (comp_choice=="scissor" and user_choice=="rock")):
       print("You won")
       print("The computer choice is " + comp_choice)
     else:
       print("You Lose")
       print("The computer choice is " + comp_choice)
    else:
       print("Please enter your choice correctly")
   else:
      print("Thank you")
      break


