################################################################################
# Author:Apoorva Shrivastava
# Date:4/19/2021
# Description 
'''
In this program we open a file, read the data then print a graph
to do this we use open(), .readlines, for loop, ax. functions, and define variables. 
'''
################################################################################

#import libraries
import matplotlib.pyplot as plt
import datetime

#def main
def main():
    
    
    #open file, read, and pass to value

    file1 = open('indiana_covid_19_data.txt', 'r')

    Lines = file1.readlines()
    count = 0
    test_date=[]
    cum_pos=[]
    cum_tot=0


#reading the lines and parsering values.
    for line in Lines:
        
        #set up the info for the graph
        
        daydata=line.split()
       
        d=daydata[0]
        test=daydata[1]
        positive=int(daydata[2])
        death=daydata[3].strip() 

        cum_tot=cum_tot+positive

        yy, mm, dd = d.split('-')
        dtime = datetime.date(int(yy), int(mm), int(dd))

        test_date.append(dtime)
        cum_pos.append(cum_tot/1000)

        coumt=count+1

        #create graph
    fig, ax = plt.subplots()
    ax.bar(test_date,cum_pos)
    ax.set_title('Positive COVID-19 Cases in Indiana')
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Cases (in thousands)')

    fig.autofmt_xdate()
    
    #close file 
    file1.close()
    
#recall
if __name__ == '__main__':
    main()
    plt.show()