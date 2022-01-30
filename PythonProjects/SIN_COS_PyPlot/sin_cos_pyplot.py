################################################################################
# Author:Apoorva Shrivastava
# Date:4/19/2021
# Description ...
'''
in this program we plot a sin and  cos graph together
to do this we import matlab libraries, and use numpy to get sin and cos data

'''
################################################################################

#import libraries
import numpy as np
import matplotlib.pyplot as plt  

#def main

def main():
    
    #set up graph lines

    X = np.linspace(0, 2 * np.pi)

    Y1 = np.sin(X)

    Y2 = np.cos(X)
    
    #set up graph, get axis object and figure object

    fig, ax = plt.subplots()

    ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))

    ax.set_xticklabels([r'$-\frac{\pi}{2}$','', r'$\frac{\pi}{2}$', 

                    r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])

    ax.set_ylim(-1,1)

    ax.set_yticks([-1,1])
 
    ax.set_xlim(0,7)
 

    ax.plot(X, Y1, color='r')
    ax.plot(X, Y2, color='b')

    ax.spines['top'].set_visible(False)

    ax.spines['right'].set_visible(False)

    ax.spines['bottom'].set_position('zero')


#call function
if __name__ == '__main__':
    main()
    plt.show()
