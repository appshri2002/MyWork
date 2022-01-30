################################################################################
# Author: Apoorva Shrivastava
# Date: 3/13/2021
# Description This program uses the directinal code to move the
#turtle through the maze and display it
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    bgpic('maze.png')
    shape('turtle')
    color('green')
    width('5')
    step = 12
    # --------------------------------------------------------------------------

    # Write your code here
    forward(11) #move forward 11 pixals
    right(90) #move to the south
    forward(82)# move forward 82 pixals
    right(90) #move to the west
    forward(72)#move forward 72 pixals
    left(90) #move to the south
    forward(25)
    left(90) # east
    forward(50)
    right(90) #south
    forward(22)
    left(90) #east
    forward(21)
    right(90) #south
    forward(73)
    left(90) #east
    forward(50)
    right(90)#south
    forward(25)
    left(90) #east
    forward(145)
    left(90) # north
    forward(45)
    right(90) # east
    forward(20)
    left(90) # north
    forward(185)
    right(90) #east
    forward(30)

# Don't change this
if __name__ == '__main__':
    main()
    done()
