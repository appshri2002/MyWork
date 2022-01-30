################################################################################
# Author: Apoorva Shrivastava
# Date: 3/29/2021
# Description 
'''
In this program we fid the min,max, sum, and average of a list.
We used two functions. One is called in the other. 
The user is required to input the numbers for the list. 
We used list, min, max, sum, format, and .appends. We also used a while loop.
'''
################################################################################

#define the function to be called. 
def get_number_list():
    
    #create a new empty list. 
    a_list=[]
    
    #create a counter to user as a conrtol for the while loop.
    count=1
    
    #while loop to get 10 inputs. 
    while count!=11:
        fc= "  Enter number"+format(count,">-3.0f")+" of 10: "
        a= float(input(fc))
        
        #adds the input to the list. 
        a_list.append(a)
        count+=1
        
        #list is returned
    return a_list

#define main function where we will call the other function 
def main():
    
    #call the function
    a_func= get_number_list()
    
    #get the min,max,sum,a and average of the list.
    a=f"{min(a_func):.2f}"
    b=f"{max(a_func):.2f}"
    c=sum(a_func)
    d=f"{(c/len(a_func)):.2f}"
    newc=f"{c:.2f}"
    
    #print
    print("Lowest number: "+a)
    print("Highest number: "+b)
    print("Total: "+newc)
    print("Average: "+d)


if __name__ == '__main__':
    main()
