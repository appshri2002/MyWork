################################################################################
# Author: Apoorva Shrivastava
# Date: 03/01/2021
''' This program asks the user to enter a starting value, increase rate and number of days
to calculate and predict a rough estimate of an organisms population.
'''
################################################################################
#This defines the function main.
def main():
    #here we asks the user for an input and convert it into a float
    start=float(input("Starting number, in million: "))
    increase= float(input("Average daily increase, in percent: "))
    days= float(input("Number of days to multiply: "))
    #here we are assigning a value to the constraint.
    daycount=1
    #printing the title
    print('Day   Approx. Pop')
    #setting up the while loop
    while daycount<=days:
        #calculating the population, printing and increasing the constraint. 
        pop= start*((1+(increase/100))**(daycount-1))
        print(format(daycount,">-3.0f"),format(pop,">-13.4f"))
        daycount+=1
 #recalling the function.        
main()
        