################################################################################
# Author: Apoorva Shrivastava
# Date: 02/28/2021
# This prgram asks the user to input a number of years and the rain for the month.
#It uses while loops and if statements to calculate the average and total inches. 
################################################################################
#This is to define the main function. 
def main():
    #This asks the users to input the number of years and converts that into an integer. 
    year_no= int(input("Enter the number of years: "))
    #The following sets the conditional values.
    raintotal=0
    average=0
    count=1
    rain=0
    totalmonthcon=0
    moncount=1
    #This is an array of the months.
    months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
#Here we have an if satetment that tells the program what to do when the input is 1 or greater.     
    if year_no>=1:
        #Here we have a while loop that tells the program what to do when the count satisfies the set condition.
        while count<=year_no:
            print("  For year No.",count)
            count+=1
            #This is the second while loop which deals with the months. 
            while moncount<=12:                
                #The following asks the user for an input which will be converted into a float. 
                rain= float(input("    Enter the rainfall for "+months[moncount-1]+".: "))
           #The following if statement tells the programmer what to do when the rain value is smaller than 0
                if rain<0:
                    print("    Invalid input, please try again.")
                  
                else :
                    moncount+=1
                    raintotal+=rain
                    totalmonthcon+=1 
            moncount=1
        print("There are", totalmonthcon,"months.")
        print(f"The total rainfall is {raintotal:.2f} inches.")
        average=raintotal/totalmonthcon
        print(f"The monthly average rainfall is {average:.2f} inches.")
        #This is in case an invalid input is entered. 
    elif year_no<1:
        print("Invalid input.") 
  #This is to recall the function.
main()
        
            
                
                
                
                
                
                
                
                
          