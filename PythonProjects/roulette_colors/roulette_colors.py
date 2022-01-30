################################################################################
# Author: Apoorva Shrivastava
# Date: 02/21/2021
# This program takes in number from the user and prints out a corresponding color.
# The only take values between 0 and 36
################################################################################
#Defining the fucntion
def main():
    #Asking user for input
    conum= int(input("Please enter a pocket number: "))
    #Creating condition for when input is invalid.
    if conum < 0 or conum> 36:
        print("  Invalid Input!")
        #creating condition for when the input is to equal to green. 
    elif conum == 0:
        print("  Pocket", conum, "is green.")
        #Creating condition for when the input is within 1 and 10.
    elif 1<= conum <=10:
        #Creating a condition to assign color based on odd or even.
        if (conum % 2) == 0:
            print("  Pocket", conum, "is black.")
        else:
            print("  Pocket",conum,"is red.")
            #creating condition for when nuber is within the 11 to 18 range.
    elif 11<= conum <=18:
        if (conum % 2) == 0:
            print("  Pocket", conum, "is red.")
        else:
            print("  Pocket",conum,"is black.")   
            #creating condition for when input is in 19 to 28 range.
    elif 19<= conum <=28:
        if (conum % 2) == 0:
            print("  Pocket", conum, "is black.")
        else:
            print("  Pocket",conum,"is red.")  
            #creating condition for when input is in 29 to 36 range.
    elif 29<= conum <=36:
        if (conum % 2) == 0:
            print("  Pocket", conum, "is red.")
        else:
            print("  Pocket",conum,"is black.") 
            #calling function
main()