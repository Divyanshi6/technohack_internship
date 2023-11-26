#""""""""""""""""""""""""""""""""""""""""""""""""ROCK PAPER AND SCISSOR GAME""""""""""""""""""""""""""""""""""""""""""""""""

import random

while True:
  print("          [ Welcome to the rock ,paper and scissor game with computer]           ")
  
  print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
       "(1) Rock vs Paper -> Paper wins  \n"
       "(2) Rock vs Scissors -> Rock wins \n"
       "(3) Paper vs Scissors -> Scissor wins \n")
  
  options=["rock","paper","scissor"]
  print("Let's begin the game.") 

  user_choice=input("make a choice from (rock/paper/scissor): ")  

  if user_choice!="rock" and user_choice!="paper" and user_choice!="scissor":
    print("Invalid choice")
    user_choice=input("Please make a valid choice from ")
    
  computer_choice=random.choice(options)
  print("You choose= ",user_choice)
  print("Computer choose= ",computer_choice)

  if user_choice==computer_choice:
      print("Oops!, it's a tie match.")
  elif (user_choice=="rock" and computer_choice=="scissor") and  (user_choice=="paper" and computer_choice=="rock") and (user_choice=="scissor" and computer_choice=="paper"):
      print("WELL DONE, you win")            
  else:
      print("BAD LUCK, computer win") 

  play_again=input("Do you want to play again: (yes or no) ? \n ")
  if play_again=="no":
     print("Thanks for playing!, goodbye see you again")
     break

