################################################################################
# Author: Apoorva Shrivastava
# Date: 02/17/2021
#This program is to convert seconds into min, hours, and days. 
#It asks the user to input seconds and then tries to match it to a category to be sorted into
#It is then calculated accordingly and the output is printed.
################################################################################
#The following is to define the function main.
def main():
     #This asks the user to input a number of seconds.
     time= int(input("Please enter a time in seconds. "))
     
    # minute= time % 3600 // 60
     #hours= time % 86400 // 3600
     #day= time // 86400
     #Here we introduce a series of if statements to produced an output according to the input. The first one is based on if the input is less than 0.
     if time < 60:
          print("  The number of seconds is less than one minute.")
          #Here we try to see if the input is between 60 and 3600. If it is we calculate the minutes and seconds.
     elif time >= 60 and time < 3600:
          m= time//60
          s= time % 60
          #This is the response for if there are 0 seconds but a certain amount of miutes.
          if s ==0:
               print(f"  {time:,} seconds is:",f"{m:,} minute(s).")
          else:
               print(f"  {time:,} seconds is:",f"{m:,} minute(s) and",f"{s:,} second(s).")
     #This is for the number of seconds can but put into an hour. Under the if statement we have the calculations for hours, min, and sec.
     elif time >= 3600 and time < 86400:
          h= time//3600
          m= time % 3600 // 60
          s= (time % 3600) % 60
          #The following if statements are the responses if there are 0 min or seconds or both. 
          if m == 0 and s == 0 and h > 0:
               print(f"  {time:,} seconds is:", f"{h:,} hour(s).")
          elif m == 0 and s > 0 and h > 0:
               print(f"  {time:,} seconds is:", f"{h:,} hour(s) and",f"{s:,} second(s).")
          elif s == 0 and m>0 and h > 0:
               print(f"  {time:,} seconds is:", f"{h:,} hour(s) and",f"{m:,} minute(s).")
          else:
               print(f"  {time:,} seconds is:", f"{h:,} hour(s),",f"{m:,} minute(s) and", f"{s:,} second(s).")
               #The following is for is the amount of seconds can be put into days.
     elif time >= 86400:
          #These are the calculations for the days, minuets, hours, and seconds. 
          d= time// 86400
          h= time % 86400 //3600
          m= time % 3600 // 60
          s= (time % 3600) % 60  
          #these are a series of responses that are to happen if there are 0 min, hours, and/or seconds. 
          if m == 0 and s == 0 and h == 0 and d > 0:
               print(f"  {time:,} seconds is:", f"{d:,} day(s).")
          elif m == 0 and s == 0 and d > 0 and h > 0:
               print(f"  {time:,} seconds is:", f"{d:,} day(s) and",f"{h:,} hour(s).")
          elif m == 0 and h > 0 and s > 0 and d > 0:
               print(f"  {time:,} seconds is:",f"{d:,} day(s),", f"{h:,} hour(s) and",f"{s:,} second(s).") 
          elif m == 0 and h == 0 and s > 0 and d > 0:
               print(f"  {time:,} seconds is:",f"{d:,} day(s) and",f"{s:,} second(s).")            
          elif s == 0 and d > 0 and h > 0 and m > 0:
               print(f"  {time:,} seconds is:",f"{d:,} day(s),", f"{h:,} hour(s) and",f"{m:,} minute(s).") 
          elif s == 0 and d > 0 and h == 0 and m > 0:
               print(f"  {time:,} seconds is:",f"{d:,} day(s) and",f"{m:,} minute(s).")          
          elif h == 0 and d > 0 and s > 0 and m > 0:
               print(f"  {time:,} seconds is:",f"{d:,} day(s),",f"{m:,} minute(s) and", f"{s:,} second(s).")            
          else:
               print(f"  {time:,} seconds is:", f"{d:,} day(s),",f"{h:,} hour(s),",f"{m:,} minute(s) and", f"{s:,} second(s).")
main()