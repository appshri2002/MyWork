################################################################################
# Author: Apoorva Shrivastava
# Date:3/6/21
# Description The following code followd the provided tempelate. 
#It calls a function within a fucntion. 
#The first function gives the user the option to input the time and has the formula
#to calculate the distance.
#The ceond function prints everything with structure and loops it. 
################################################################################

# Write function(s) here
#define first function
def falling_distance(t):
    #calculate the distance
    d=1/2*9.81*t**2
    #return distance
    return d
def main():
    print("Time (s)  Distance (m)")
    print("----------------------")
    #loop
    for i in range(1,11):
        new= falling_distance(i)
        #print formatted answer
        print(format(i,">-8.0f"),format(new,">-13.2f"))

if __name__ == '__main__':
    main()
