################################################################################
# Author: Apoorva Shrivastava
# Date: 3/29/2021
# Description 
'''
Here we rolld two dices 900000 times and print a percentage of the numbers
that show up. We have called two functions, used list.count,list.append
while loop, return function, and  list definition function.
'''
################################################################################

#import randome, and use r inplace of random
import random as r


#define function to be called
def roll_d6():
    roll=r.randint(1,6)
    return roll

#define second function to be called
def  get_2d6_rolls(d):
    
    #creating a blank list
    a_list=[]
    count=1
    
    #creating a while loop to run the program a certain number of times. 
    while count <=d:
        
        #calling function
        a= roll_d6()
        b= roll_d6()
    
        c=a+b  
        
        #add c to the list
        a_list.append(c)
        count+=1
    return a_list

#define main and call other functions
 
def main():
    
    #calling function
    call=get_2d6_rolls(900000)
    
    print("Roll  Frequency")
    ctr=2
    
    #printing table
    while ctr<=12:
        perc= (call.count(ctr)/900000)*100
        print(format(ctr,">-3.0f"),format(perc,">-8.2f")+"%")
        
        ctr+=1
   


if __name__ == '__main__':
    main()
