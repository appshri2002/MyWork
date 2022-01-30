#Description Tittle comment: leap_year: This program helps the user find out if the year entered is a leap year or not. 
#Then we check to see if the year is divisible by 100. If it is, we check to see if it is divisible by 400. If it is, then its a leap year.
#If it is not divisible by 100 we chekc to see if it is by 4. If ti is then it is a leap year, else it is not. 
#This is done by prompting the.Author: Apoorva Shrivastava, Date: 2/16/2021
def leapyear():
    #This asks for the user to input the year
    year= int(input("Please input a year: "))
    #this check to see if the year is divisible by 100
    if year%100==0:
        #This checks if the year is divisible by 400
        if year%400==0:
            #If the year is divisible by 400 the following will be the output
            print(f"In the year {year}, there are 29 days in February.")
        else:
            #If the year si not divisible by 400 the following will be the output
            print(f"In the year {year}, there are 28 days in February.")
            #if the year is not divisible by 100 it will be ckecked with 4
    elif year%4==0:
        #if year is divisible by 4 this will be the output
        print(f"In the year {year}, there are 29 days in February.")
        
    else:
        #if the year is not divisible by 4 this will be the output
        print(f"In the year {year}, there are 28 days in February.")
leapyear()
