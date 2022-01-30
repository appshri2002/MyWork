################################################################################
# Author: Apoorva Shrivastava
# Date: 4/5/2021
# Description 
'''
Here we translate phonenumbers with letters into complete numbers
We used list, maketrans function, .translate function, called function

'''
################################################################################

#defining a function to be called. 
def convert_number(a):
    
    #creating a list to use for the translations
    phone_lists=str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz","2223334445556667777888999922233344455566677778889999")
    
    #retruning the translations
    return a.translate(phone_lists)    
    

#defining main function
def main():
    
    #asking user for input and converting to string
    tele_no=str(input("Enter a telephone number: "))
    #calling function
    call=convert_number(tele_no)
    print("The phone number is",call)


#calling main 
if __name__ == '__main__':
    main()
