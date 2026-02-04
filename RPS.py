#RPS.py
#Name: Nidhi Agarwal
#Date: 02/04/2026
#Assignment: Create a game Rock, Paper, Scissors with the system
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  play_again = "Y"
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  

  while play_again in ('Y','y'):
   system_choice = random.choice(['R','P','S'])
  
   while True:
      user_choice=input("Enter your choice R for Rock, P for Paper, S for Scissors : ")
      if user_choice not in ('R', 'P', 'S','r','s','p'):
          print ("Invalid choice: please choose 'R', 'P' or 'S'")
          continue

      if user_choice == system_choice:
       print("Its a tie! ")
       ties +=1
      elif (user_choice == 'R' or 'r' and system_choice == 'S') or\
           (user_choice == 'P' or 'p' and system_choice == 'R') or\
           (user_choice == 'S' or 's' and system_choice == 'P'): 
           print (f"System choice {system_choice}   You Win! ")
           wins +=1
      else:
        print (f"System choice {system_choice}   You Lose ! ")
        losses +=1
      break
   play_again = input("Do you want to play again? (Y/N):")
           
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()

