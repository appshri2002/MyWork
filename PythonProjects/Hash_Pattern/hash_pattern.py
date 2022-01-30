################################################################################
# Author: Apoorva Shrivastava
# Date: 02/24/2002
# This program asks the user to input a valuse which will be converted into an integer and assigned to the variable lines.
#The program will then spit out two hashes while increasing the space between them untill it reaches the value inputted by the user.

################################################################################
#This is to define the main function. 
def main():
    #This asks for the user to input a number that is to be converted into an integer and assigned to the variable lines. 
    lines=int(input("Enter the number of lines: "))
    #Here we are assigned values to vairables. Two are num values where one is the space to be printed between hashes. 
    space1=0 
    space2=0
    actspace=" "
    #This while loop sets up the condition that will start the code 
    while space1<lines :
        #This sets up the second while loop.
        while space2==space1:
            #This is to increase the space length. 
            hashspace= actspace*space1
            space2+=1
        print(f"#{hashspace}#")
        space1+=1
#This recalls the function.
main()
        