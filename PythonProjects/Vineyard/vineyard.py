import math
def vineyard():
    print('Enter the following quantities in feet.')
    R= float(input('  How long is this row? '))
    E= float(input('  How wide is the end-post assembly? '))
    S= float(input('  How much space should be between the vines? '))
    V= math.floor((R-2*E)/S)
    NV= str(V)
    print("")
    print('This row has enough space for '+NV+' vine(s).')
vineyard()
