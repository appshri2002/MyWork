################################################################################
# Author:Apoorva Shrivastava 
# Date: 4/5/2021
# Description
'''
This program reads the txt file created by anouther program 
and returns the max, min, sum,average, and amount of lines read. 
we used for loop, with open function, max, min, len, sum, append,
and print function
'''
################################################################################
 
#defin main function    
def main():
    
    #create a empty list
    a_ray=[]
    
    #opet txt file and add contents to list
    with open('random_numbers.txt') as fo:
        
        for line in fo:
            a_ray.append(int(line))
            
            #print
    print(f'{len(a_ray):,.0f}', "numbers were read from the file.")
    print("Max:",max(a_ray))
    print("Min:",min(a_ray))
    print("Sum:",f"{sum(a_ray):,.0f}")
    print("Avg:",f"{(sum(a_ray)/len(a_ray)):,.1f}")
          

#recall main function
if __name__ == '__main__':
    main()
