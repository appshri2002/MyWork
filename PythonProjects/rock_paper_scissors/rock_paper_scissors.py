################################################################################
# Author: Apoorva Shrivastava
# Date: 3/22/2021
'''
This program is a game of rock paper and scissors.
The computer will choose one of the option as well as the user.
The program presents is as a sum and asks the user for an input.
The program responds based on the users response.
This program uses random function and if else statements.
'''
################################################################################

#impurt random and represent it as r
import random as r

#define function to pick random choice
def get_computer_choice():
    a_list=("rock","paper", "scissors")
    return r.choice(a_list)

#define function to have user enter their option
def get_player_choice():
    control=0
    while control!=1:
        choice=input("Choose rock, paper, or scissors: ")
        if choice!="rock" and choice!="paper"and choice!="scissors":
            print("You made an invalid choice. Please try again.")
        else:
            control=1
    return choice

def get_winner(a,b):
    
    result=""                       
        
    

    if a==b:
        result="tie"
      
        
        
    elif a=="rock" and b=="paper":
        result="player"
        print("paper beats rock")
        
        
    elif a=="rock" and b=="scissors":
        
        result="computer"
        print("rock beats scissors")
        
        
        
    elif a==b:
        result="tie"
        
        
        
    elif a=="paper" and b=="scissors":
        
        result="player"
        
        print("scissors beat paper")
        
      
        
        
    elif a=="paper" and b=="rock":
        
        result="computer"
        print("paper beats rock")
        
        
        
    elif a=="scissors" and b=="rock":
        
        result="player"
        print("rock beats scissors")
        
        
        
    elif a=="scissors" and b=="paper":
        
        result="computer"
        print("scissors beat paper")
        
        
    elif a==b:
        result="tie"
        
    return result
    
#define main where we will call get computer choice
def main():
    
    #establishing a count so we can use a while loop to keep this entire thing going when we get a tie
    count=0
    while count==0:    
        
        
        #calling functions
        a=get_computer_choice()
        b=get_player_choice()
        
        print("  The computer chose",a+", and you chose",b+".")
        
        
        result=get_winner(a,b)
        if result=="tie":
            print("  Its a tie. Starting over.")
            
        
        elif result=="player":
            print("  You won the game!")
            count=1
        
        else:
            print("  You lost.  Better luck next time.")
            count=1
            
            
            
         
            
    print("Thanks for playing.")

if __name__ == '__main__':
    main()