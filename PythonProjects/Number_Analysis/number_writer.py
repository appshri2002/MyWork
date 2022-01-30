################################################################################
# Author:Apoorva Shrivastava
# Date: 4/5/2021
# Description
'''
this program only uses one function. It asks user for an input and prints that many numbers
it prints numbers between 1 to 500 in a text file. We have used w which truncates a 
prexisting file. In this program we used randome functions, input, with open
, for loop, and .write.
'''
################################################################################

#import random  and assigning it to r
import random as r 

#defining main function
def main():
    
    #asking user for input
    lines=int(input("Enter the number of random numbers to be written to the file: "))
    
    #open file
    with open('random_numbers.txt','w') as fo:
        
        #print lines.
        for x in range(1,lines+1):
            fo.write(str(r.randrange(1,501))+'\n')
            

    
#call function
if __name__ == '__main__':
    main()
