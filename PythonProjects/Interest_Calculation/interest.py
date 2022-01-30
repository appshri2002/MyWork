import math
def interest():
       print("Please enter the following quantities.")
       P= float(input('  How much is the initial deposit? '))
       r= float(input('  What is the annual interest rate in percent? '))
       n= float(input('  How many times per year is the interest compounded? '))
       t= float(input('  How many years will the account be left to earn interest? '))
       Fv= P*((1+(r/(100*n)))**(n*t)) 
       print()
     
       
       print("At the end of" , t , f"years, the account will be worth ${Fv:,.2f}.")

interest()