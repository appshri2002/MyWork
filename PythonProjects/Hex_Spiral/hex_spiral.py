################################################################################
# Author: Apoorva Shrivastava
# Date: 3/15/2021
# Description: This code imports functions from tutle to build a hexigon.
# It uses a while loop to keept he program running untill conditions are met. 
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width('5')
    # --------------------------------------------------------------------------

    # Write your code here
    count=1 # This variable maintains the count
    while count<=39: #while loops keeps the program running
        forward(6*count) # move the line forward but increase by six pixals every loop
        right(60) #turn 60 deg clockwise
        count+=1

# Don't change this
if __name__ == '__main__':
    main()
    done()
