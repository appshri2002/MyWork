################################################################################
# Author:Apoorva Shrivastava
# Date:4/5/2021
# Description 
'''
In this program we opened a file and counted the lines, amt of words, and
avaergae words per line. We used with open as function, for loop, and print function.
There is no user input required. 
'''
################################################################################ 



#defning main function   
def main():
    
    #setting up the counters.
    line_count=0
    word_count=0
    
    #oppening the text file
    with open('rumpelstiltskin.txt') as fo:
        
        #using for loop to count lines and words
        for line in fo:
            line_count+=1
            word=line.split()
            word_count+=len(word)
            #for word in line:
                #word_count+=1
    print("Total number of words:",word_count)
    print("Total number of lines:",line_count)
    
    #calculating average
    avg= f"{word_count/line_count:.1f}"
    print("Average number of words per line:",avg)
            
    
#calling main 

if __name__ == '__main__':
    main()
