################################################################################
# Author: Apoorva Shrivastava
# Date: 02/21/2021
# This program takes in inputs and calculates the fluid mechanics accordingly
# calculations vary on the temperature entered. 
################################################################################
#This is to define the function.
def main():
    #This asks the user to put in inputs that will be converted to floats.
    V= float(input("Enter the velocity of water in the pipe: "))
    d=float(input("Enter the pipe's diameter: "))
    #Special code used for deg symbol.
    v=(float(input("Enter the temperature in \u00B0C as 5, 10, or 15: " )))
   # Re = (V*d)/v
   #This is to convert v into a string so that it can eb printed without extra space. 
    sv= str(v)
   #This sequence is for if the user selected 5 deg.
    if v == 5:
        Re= (V*d)/(1.49*10**(-6))
        #formats the answer in scientific form.
        Re_1= format(Re, "1.2e")
        
   #     print("The Reynolds number for flow at", V,"m/s in a ", d,"m diameter pipe at ",v+"\u00B0 is"+Re_1+".")
        print("The Reynolds number for flow at",V,"m/s in a",d,"m diameter pipe at "+sv+"\u00B0C is "+Re_1+".")
        #The folowing sequence is for if the yser selected 10 deg.
    elif v == 10:
        Re= (V*d)/(1.31*10**(-6))
        Re_1= format(Re, "1.2e")
        
        print("The Reynolds number for flow at",V,"m/s in a",d,"m diameter pipe at "+sv+"\u00B0C is "+Re_1+".")
        #the folowing sequence is for if the user selected 15 deg.
    else : 
        Re= (V*d)/(1.15*10**(-6))
        Re_1= format(Re, "1.2e")
      
        print("The Reynolds number for flow at",V,"m/s in a",d,"m diameter pipe at "+sv+"\u00B0C is "+Re_1+".")
        #this is to call the function.
main()
    
