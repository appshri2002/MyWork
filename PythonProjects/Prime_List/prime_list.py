################################################################################
# Author: Apoorva Shrivastava
# Date: 3/8/21
# Description The following asks the user to input a number and prints all the prime
# numbers up till it. 
################################################################################

# Write function(s) here
#define first function
def is_prime(num):
    if num==1:
        return False
    #for loop to help find a prime number
    for x in range(2,int(num**.5)+1):
        if num % x == 0:
            return False
       
    else:
        return True
#define the function main
def main():
    #define a new list
    a_list=[]
    #ask user for input
    num=int(input("Enter a positive integer: "))
    for x in range(1,num+1):
           
        new_p = is_prime(x)
        
        if new_p:
            #print and format list. 
            a_list.append(str(x))
    new_list=', '.join(a_list)
    
    print("The primes up to",num,"are: "+new_list)
        
        

#recall function main
if __name__ == '__main__':
    main()
        
                
                
        
