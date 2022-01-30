################################################################################
# Author: Apoorva Shrivastava
# Date: 2/26/2021
# Description 
'''
In this program we get a 6,10,and 20 sided die to be rolled 10 times. 
It is all hardcoded. In this program we created a class called Dice and created
methods called roll and n_roll to establish the sides of the die and the amount
of times it is to be rolled respectivly. 
'''
################################################################################

#Import randome from library
import random  

#Define class Dice    
class Dice:
    
    #Initialize the parameters
    def __init__(self, sides):
        self.sides=sides
    
    #method to retrun a random number or roll the die once.     
    def roll(self):
        return random.randint(1, self.sides)
    
    #method to call the roll method a certain amount of times.
    def n_rolls(self, a_num):
        l=[]
        for i in range(0,a_num):
            l.append(self.roll())
        
        
        print("Rolling a "+str(self.sides)+" sided die "+str(a_num)+" times: ",end="")
        print(*l,sep=', ')


             
    
#define the main function where we call the class Dice    
def main():
    
    #initiating objects
    
    #Roll 6 sided die 10 times
    A= Dice(6)
    A.n_rolls(10)
    
    #roll 10 sided die 10 times
    A= Dice(10)
    A.n_rolls(10) 
    
    #roll 20 sided die 10 times
    A= Dice(20)
    A.n_rolls(10)    
    

#call main function
if __name__ == '__main__':
    main()
