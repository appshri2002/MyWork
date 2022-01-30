################################################################################
# Author: Apoorva Shrivastava
# Date: 3/22/2021
'''
This program produces two random integers.
One is two digits and the other is three. 
The program presents is as a sum and asks the user for an input.
The program responds based on the users response.
This program uses random function and if else statements.
'''
# of Purdue students of year 1869
################################################################################

#impurt random and represent it as r
import random as r

def random_number(a):
    if a==2:
        b= r.randint(10,99)
    elif a==3:
        b=r.randint(100,999)
    return b

#define function main
def main():
    
    #assign the random integers to variables.
    B=random_number(2)
    C=random_number(3)
    
    #print the values in a sum like format
    print("  ",B)
    print("+",C)
    print("-----")
    
    #ask user to input answer
    ans=int(input("= "))
    answer=str(C+B)
    if ans!=(B+C):
        print("Incorrect. The correct answer is "+answer+".")
    else:
        print("Correct -- Good Work!")

if __name__ == '__main__':
    main()
