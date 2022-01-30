################################################################################
# Author:Apoorva Shrivastava
# Date: 3/8/21
# Description The following program asks the user to input grades
# it returns the corresponding letter grade and calculates the average. 
################################################################################

# Write function(s) here
#define a variable
score=0
#define other programs
def get_valid_score():
    while 1==1:
        score=float(input("Enter a score: "))
        if 0<=score<=100:
            return score
        else:
            print( "Invalid Input. Please try again.")
def calc_average(score_list):
    #setting a variable to calculate average later. 
    total=0.0
    #for loop to calculate total and later average. 
    for x in score_list:
        total+=x
    avg= total/len(score_list)
    return avg
   # print(f'The average score is {avg:.2f}.')
    
def determine_grade(uscore):
    #tells program what letter grade to print for different kinds of input. 
    if 0<=uscore<60:
        return "F"
    elif 60<=uscore<70:
        return "D"
    elif 70<=uscore<80:
        return "C"
    elif 80<=uscore<90:
        return "B"
    elif 90<=uscore<=100:
        return "A"
    
  #defininf the function named main.   

def main():
    a_list=[]
    for x in range(5):
        score_1=get_valid_score()
        grade1=determine_grade(score_1)
        print(f"The letter grade for {score_1:.1f} is "+grade1+".")
        a_list.append(score_1)
    print(f"The average score is {calc_average(a_list):.2f}.")
    

if __name__ == '__main__':
    main()
