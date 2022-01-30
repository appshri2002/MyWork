################################################################################
# Author:Apoorva Shrivastava
# Date:4/18/2021
# Description ...
'''
In this program the user is prompted to enter the sales.
Thoose sales are then displayed on a pi chart. 
In this function we imported matplotlib, used an array, used for loop, 
and used fig and ax function.
'''
################################################################################

#import matplotlib
import matplotlib.pyplot as plt
#%pylab inline

#def main    
def main():
    
    
    #here we are getting the fig and ax object
    fig, ax = plt.subplots()
    
    #define array

    
    data = []
    months=['January','February','March','April','May','June','July','August','September','October','November','December']
    c = ['#4D4038','#BAA892','#5B6870','#6E99B4','#A3D6D7','#085C11','#849E2A','#C3BE0B','#E9E45B','#6B4536','#B46012','#FF9B1A']

#for loop to get user and add to array

    for i in range(len(months)):
        d=int(input('Enter the sales for '+months[i]+': '))
        data.append(d)
    #code for the physical appearence of graph
    ax.pie(data, colors=c,labels = months)
    ax.set_title('Monthly Sales Values')
    fig.show(months)
    
if __name__ == '__main__':
    main()
    plt.show()
