#===============================================================
# Your Name & Lab Section: Apoorva Shrivastava, Thursday 9:30
# Your Purdue Email: shrivas2@purdue.edu
# Program Description: In your own words, provide a brief description of the program in 1-2 sentences.
'''
In this program we open two files. One to read and one to write. 
From the first file we take in information and divive it into 
two lists that are then written into the second file. We also calculate the max
and min of one of the lists and print that information into the second lists
we also set up an exception.

'''
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================


#define main function
def main():
    
    #set up try
    try:
        
        #open file and set up empty list
        file1= open('input.txt','r') 
        Names=[]
        Scores=[]
        file2= open('output.txt.','w')
        
      # go through the lines and divide into two lists that are then written into second file 
        for line in file1:
            Temp= line.split(',')
            
            Names.append(Temp[0])
            Scores.append(float(Temp[1]))
        Maximum=max(Scores)
        Minimum=min(Scores)
        file2.write("Maximum score is : "+str(Maximum)+"\n")
        for num in range(0,len(Scores)):
            if Scores[num]== Maximum:
                file2.write(str(Names[num])+", "+str(Scores[num])+"\n")
                
        file2.write("Minimum score is : "+str(Minimum)+"\n")
        for num in range(0,len(Scores)):
            if Scores[num]== Minimum:
                file2.write(str(Names[num])+", "+str(Scores[num])+"\n")        
        
        print("Printing every content in the file...")
        print(Names)
        print(Scores)
         
   
    #set up exception            
    except FileNotFoundError:
        print("The program failed to open the file. Make sure the followings:")
        print("\tThe file to read is located in the same folder as this program is!")
        print("\tThe file's name is spelled correctly")
#call main
main()