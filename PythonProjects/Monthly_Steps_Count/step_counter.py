################################################################################
# Author:Apoorva Shrivastava
# Date: 4/5/2021
# Description
'''
in this program we open a file, read it, add its contents to a list
and print the average steps taken a month. 
We used lists, append, with open, print, and format
'''
################################################################################
 

#defin main function   
def main():
    
    #create an empty list
    
    a_ray=[]
    print("The average steps taken each month were:")
    
    #open file and ass steps to list
    with open('steps.txt') as fo:
        for steps in fo:
            a_ray.append(int(steps))

            #print averages
    print("   January :",f"{sum(a_ray[0:31])/31:.1f}")
    print("  February :",f"{sum(a_ray[31:59])/28:.1f}")
    print("     March :",f"{sum(a_ray[59:90])/31:.1f}")
    print("     April :",f"{sum(a_ray[90:120])/30:.1f}")
    print("       May :",f"{sum(a_ray[120:151])/31:.1f}")
    print("      June :",f"{sum(a_ray[151:181])/30:.1f}")
    print("      July :",f"{sum(a_ray[181:212])/31:.1f}")
    print("    August :",f"{sum(a_ray[212:243])/31:.1f}")
    print(" September :",f"{sum(a_ray[243:273])/30:.1f}")
    print("   October :",f"{sum(a_ray[273:304])/31:.1f}")
    print("  November :",f"{sum(a_ray[304:334])/30:.1f}")
    print("  December :",f"{sum(a_ray[334:365])/31:.1f}")
    
        
#call main function
if __name__ == '__main__':
    main()
