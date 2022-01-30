################################################################################
# Author: Apoorva Shrivastava
# Date: 3/15/21
# Description here we use the turtle program to print hello turtle
#there are no inputs from the user
################################################################################

# Don't change this
from turtle import *

def draw_e():
    # Write this function
    penup()
    
    forward(-30)
    left(90)
    forward(30)
    pendown()
    right(90)
    forward(60)
    left(90)
    circle(30, 315)
    penup()
    setheading(-90)
    forward(15)
    
  # this is for h
def draw_h():
    # Write this function
    left(90)
    forward(120)
    penup()
    right(180)
    forward(65)
    left(125)
    pendown()
    
   # forward(35)
    circle(-30, 70)
    setheading(90)
    right(180)
    forward(55)
    #forward(35) '''
    '''  penup()
    left(90)
    forward(120)
    pendown()
    right(180)
    forward(120)
    penup()
    #left(180)
    forward(60)
    pendown()
    forward(35)
    circle(-30, 180)'''
      
    
    
def draw_l():
    # Write this function
    penup()
    left(90)
    forward(120)
    pendown()
    right(180)
    forward(120)
def draw_o():
    # Write this function
    circle(30, 360)
def draw_r():
    # Write this function
    left(90)
    forward(60)
    penup()
    right(180)
    forward(10)
    left(120)
    pendown()
  #  forward(2)
    circle(-30, 60)
    setheading(-90)
    
    
def draw_t():
    # Write this function
    left(90)
    forward(120)
    penup()    
    right(180)
    forward(30)
  #  pendown()
    left(90)
    forward(30)
   # penup()
    left(180)
    pendown()
    forward(60)
    penup()
    right(180)
    forward(30)
    right(90)
    forward(90)
def draw_u():
    # Write this function
    penup()
    left(90)
    forward(60)
    pendown()
    right(180)
    forward(35)
    circle(30, 180)
    forward(35)
    penup
    right(180)
    forward(35)
    pendown()
    forward(25)
def main():

    # Don't change this block --------------------------------------------------
    setup(600, 400)
    width(9)
    # --------------------------------------------------------------------------

    # Write your main function code here
    penup()
    goto(-200,30) #this all decides the position
    pendown()
   
   #for h
   
    draw_h()
    setheading(0)
    penup()
    forward(60)
    
    pendown()
 #for e
    
    draw_e()
    setheading(0)
    forward(60)
    
   #for l
    
    draw_l()
    setheading(0)
    penup()
    forward(60)
    pendown()
    
    #for l
    
    draw_l()
    setheading(0)
    penup()
    forward(60)
    pendown()
    
    #for o
       
    draw_o()
    penup()
    goto(-200,-150)
    pendown()
    
    #for t
    
    draw_t()
    setheading(0)
    penup()
    forward(30)
    
   #for u 
    
    draw_u()
    setheading(0)
    penup()
    forward(30)  
    pendown()  
    
    #for r
    
    draw_r()
    setheading(0)
    penup()
    forward(30)  
    penup()
    
    right(90)
    forward(60)
    right(90)
    left(180)
    pendown()
   
   #for t
   
    draw_t()
    setheading(0)
    penup()
    forward(60)  
  #  left(90)
    
    pendown()
    
       
    #for l 
    
    draw_l()
    setheading(0)
    penup()
    forward(60)  
    pendown()   
   
   #for e 
   
    draw_e()
    setheading(0)
    penup()
    forward(30)  
    pendown()    
    
# Don't change this
if __name__ == '__main__':
    main()
    done()
