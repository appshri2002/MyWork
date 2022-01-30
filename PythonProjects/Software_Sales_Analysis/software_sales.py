################################################################################
# Author: Apoorva Shrivastava
# Date: 02/20/2021
# This program calculates the number
# of Purdue students of year 1869
################################################################################
def main():
    #Ask the user for input
    pakgs= int(input("Please input the number of packages to be purchased: "))
    price= (pakgs*99)
    #This is for is the input value is 0 or lower.
    if pakgs <= 0:
        print("  Invalid Input!")
    #This is the res  ponse for if the input is under 10 and over 0
    elif 0< pakgs< 10:
        print("  No discount applied.")
        print("  The final price for purchasing", pakgs,"packages is",'${:0,.2f}'.format(price)+'.')
    elif 10<= pakgs <=19:
        dprice= 0.90*price        
        print("  10% discount applied.")
        print("  The final price for purchasing", pakgs,"packages is",'${:0,.2f}'.format(dprice)+'.')
    elif 20<= pakgs <=49:
        dprice= 0.75*price
        print("  25% discount applied.")
        print("  The final price for purchasing", pakgs,"packages is",'${:0,.2f}'.format(dprice)+'.')
    elif 50<= pakgs <=99:
        dprice= 0.65*price
        print("  35% discount applied.")
        print("  The final price for purchasing", pakgs,"packages is",'${:0,.2f}'.format(dprice)+'.')
    elif 100<= pakgs:
        dprice= 0.55*price
        print("  45% discount applied.")
        print("  The final price for purchasing", pakgs,"packages is",'${:0,.2f}'.format(dprice)+'.')    
        
main()