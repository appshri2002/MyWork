#===============================================================
# Your Name & Lab Section: Apoorva Shrivastava, Thursday 9:30
# Your Purdue Email: shrivas2@purdue.edu
# Program Description: In your own words, provide a brief description of the program in 1-2 sentences.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

#define main function 
def main():
   
   
   #code for try 
    try:
        
        #open book, put contents in a list, analyze and write new contents into new file. 
        book= open('books.txt','r')
        analysis= open('book_analysis.txt','w')
        
        
        newbook= book.readlines()
        
        print("Printing contents of file...")
        print(newbook)
        
        analysis.write("=======Analysis Result=======\n\n")
        analysis.write("1. The number of books in this file: "+str(len(newbook))+"\n\n2. Titles of books which have more than two words\n\n")
        for line in newbook:
            if len(line)>2:
                analysis.write(line)
        analysis.write("\n\n3. Orginized Book Titels :\n\n")
        
        for line in newbook:
            analysis.write(str(line.title()))
        
        
        
        
        
      
            
    #in case file can not be opened.     
    except FileNotFoundError:
        print("The program failed to open the file.  Make sure of following:")
        print("\tThe file to read is located on the same program the file is!")
        print("\tThis file's name is spelled correctly")
        
#cal main function        
main()
        
        