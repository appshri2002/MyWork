################################################################################
# Author:Apoorva Shrivastava
# Date: 4/19/2021
# Description 
'''
In this program we open a file, read it, and plot the data. In oder to complete 
this we imported matplotlib, open, .readlines(), lists, for loop, .append, ax. functions. 
'''
################################################################################

#Import matplot library
import matplotlib.pyplot as plt

#def main    
def main():


    #open file
    file1 = open('2008_Weekly_Gas_Averages.txt', 'r')
    

    Lines = file1.readlines()
    
    count = 0
       
    prices=[]
    weeks=[]
    
    #for loop to go through the file and add to the lists
    for line in Lines:
        prices.append(float(line.strip()))
        count = count+1
        weeks.append(count)
    


        # set up of graph
    fig, ax = plt.subplots()

    ax.plot(weeks,prices)
    ax.set_title('2008 Weekly Gas Prices')

    ax.set_xlabel('Weeks (by number)')

    ax.set_ylabel('Average Price (dollars/gallon)')
    ax.set_ylim(1.5,4.25)
    ax.set_xlim(1,52)
    
    
    ax.grid()
 
    fig.show()
    file1.close()

  
#call function    
if __name__ == '__main__':
    main()
    plt.show()