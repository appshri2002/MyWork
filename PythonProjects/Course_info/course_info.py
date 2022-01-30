################################################################################
# Author:Apoorva Shrivastava
# Date:4/12/2021
# Description ...
'''
In this program we create a nested list and the user draws information
out of that list. We called fucntion, used .updated. print function, dict()
return and if-else
'''
################################################################################

#define fucntion to be called
def get_course_data():
    
    #define dicts
    C_info={}
    A_info=dict(instructor= "Haynes",room='3004',time= "8:00 a.m.")
    B_info=dict(instructor= "Alvarado",room='4501',time= "9:00 a.m.")
    D_info=dict(instructor= "Rich",room='6755',time= "10:00 a.m.")
    E_info=dict(instructor= "Burke",room='1244',time= "11:00 a.m.")
    F_info=dict(instructor= "Lee",room='1411',time="1:00 p.m.")
    
    #update list
    C_info.update({"CS101":A_info})
    C_info.update({"CS102":B_info})
    C_info.update({"CS103":D_info})
    C_info.update({"NT110":E_info})
    C_info.update({"CM241":F_info})
    
    return C_info
    
#def main 
def main():
    
    #rcall function
    get_data=get_course_data()
    inp=input("Enter a course number: ")
    #coding to present info
    if inp in get_data:
        info=get_data[inp]
        Room=info['room']
        Instructor=info['instructor']
        Time= info["time"]
        print("The details for course "+inp+" are:")
        print("  Instructor:",Instructor)
        print("        Room:",Room)
        print("        Time:",Time)        
        
    else:
        print(inp,"is an invalid course number.") 
   

#call function 

if __name__ == '__main__':
    main()
