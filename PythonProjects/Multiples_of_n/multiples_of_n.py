################################################################################
# Author: Apoorva Shrivastava
# Date: 3/29/2021
# Description:
'''
In the followng code we create a function that will be called. In that function we
enter a list and a number then check if the numbers in the list are divisible by
the entered number.
We used list, if statement, for loop, and .append in this assignment.
'''
################################################################################

#here we are definf the function to be called.
def multiples_of(a,b):
    #convert b into a list
    b= list(b)

    #create a new list to store the multiples
    c=[]

    #for loop to go through all the values in the list
    for x in b:

        #if statement to check divisivbility
        if x%a==0:

            #use append to add a value to a list
            c.append(x)
    #return c
    return c

#define main function
def main():

    print("Original list of numbers:")

    number_list = [19, 2940, -189, 10, 28, -58, 1, 85, 201, -15, 122, 799, 406]

    print(number_list)

    print("Numbers in the list that are multiples of 7:")


    print(multiples_of(7,number_list))




if __name__ == '__main__':
    main()
