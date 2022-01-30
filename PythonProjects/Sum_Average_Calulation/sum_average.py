################################################################################
# Author: Apoorva Shrivastava
# Date: 02/27/2021
# This program asks the user for an input and keeps going untill a negative number is put it. 
#The question is asked untill a negative number is put in and then the sum and average is calculated and printed. 

################################################################################
#This is to define the function main.
def main():
    #here we are assigning variables that are used as conditions
    list1=0
    total=0
    count=0
    #we are using a while loop to loop the question.
    while list1>=0:
        list1= float(input("Enter a non-negative number (negative to quit): "))
        total= total+list1
        count+=1
    total= total-list1
    count= count-1
        #we are using an if statement to add the find the average.
        
    if total>=0 and count>0:
        average = total/count
        print(f"Sum = {total:.2f}")
        print(f"Average = {average:.2f}")
    
    else:
        print("No input.")
    
        
    #this recalls the function. 
main()
    
        