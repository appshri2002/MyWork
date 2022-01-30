################################################################################
# Author: Apoorva Shrivastava
# Date: 3/15/2021
# Description This program takes an input from the user and 
#prints a star with thoose many points.
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()
    # --------------------------------------------------------------------------

    # Write your code here
    
    point=int(input("Enter: ")) #ask user for input and convert to integer
    A=360/point #calculate the value of A     
    B=2*A #calulate the value of B
    count=0 #Set a control variable
    setheading(A-90)
    color('black', 'pink')
    begin_fill()
    while count<point: #while loop to keep the program running until star is complete
        forward(60)
        left(180-A) #turn north
        forward(60)
        right(180-B)#turn west
        count+=1
    end_fill()
    
   


# Don't change this
if __name__ == '__main__':
    main()
    done()
