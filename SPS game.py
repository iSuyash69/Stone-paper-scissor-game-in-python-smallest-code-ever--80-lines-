#Stone paper scissor game in python
#Made by - Suyash Deshpande 

import math
import random

def game():
    print("\n\n------------------------STONE-PAPER-SCISSOR GAME--------------------------")
    print("\n\t\t\t  WELCOME to the GAME\n")
    player=input("   Enter Your NAME: ")
    print(f"\n\t\t  Welcome {player}, this is a 5 ROUND match \n\t\t\t !!!get yourself ready!!! ")
    print("\n  |  STONE - Press 1  |  PAPER - Press 2  |  SCISSOR - Press 3  |  ")
    input("\n\n  press ENTER to Begin")
    x=0             #To execute the while loop
    r=0             #To count the no. of rounds
    user1=0         #To track the score of user
    comp3=0         #To track the score of computer
    while x!=5:
        x+=1    
        r+=1
        print(f"\n\n ------ROUND-{r}------")
        user=int(input("\n Your choice:  "))
        if user==1:
            print(f"\n You chose: STONE")
        elif user==2:
            print(f"\n You chose: PAPER")
        elif user==3:
            print(f"\n You chose: SCISSOR")
        else:
            print("INVALID INPUT")

        computer=[1,2,3]
        comp2=random.choice(computer)
        if comp2==1:
            print(f" Computer chose: STONE\n")
        elif comp2==2:
            print(f" Computer chose: PAPER\n")
        elif comp2==3:
            print(f" Computer chose: SCISSOR\n")

        if user==comp2:
            print("\n\tIt's a DRAW")
            print(f"SCORE: {player}-{user1}  |  COMPUTER-{comp3}")
        elif user==1 and comp2==3:
            print("\n\tYou WON")
            user1+=1
            print(f"SCORE: {player}-{user1}  |  COMPUTER-{comp3}") 
        elif user==2 and comp2==1:
            print("\n\tYou WON")
            user1+=1
            print(f"SCORE: {player}-{user1}  |  COMPUTER-{comp3}") 
        elif user==3 and comp2==2:
            print("\n\tYou WON")
            user1+=1
            print(f"SCORE: {player}-{user1}  |  COMPUTER-{comp3}")    
        else:
            print("\n\tYou LOST")
            comp3+=1
            print(f"SCORE: {player}-{user1}  |  COMPUTER-{comp3}")
        
    if user1>comp3:
        print("\n\nCongrats!! YOU WON THE GAME")
    elif user1<comp3:
        print("\n\nYOU LOST THE GAME!! Better luck next time")
    elif user1==comp3:
        print("\n\nOH!! ITS A TIE GAME")
    
    x=input("\n\nDo you want to play again: Y/N  - ")
    while x=="y" or x=="Y":
        game()  
        break
    if x=="n"or x=="N":
        print("\n------GAME OVER------")
    

game()




    




