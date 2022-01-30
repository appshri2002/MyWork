###############################################################################
# Author: Apoorva Shrivastava
# Date: 5/9/2021
# Description 
'''
In this program we create a game. The user gets a random amount of money and
can use that for a game. They can spin the wheel to get money and they guess
the word with the consonents. They need to pay to buy the vowels. They can also quit 
the game
'''
###############################################################################
#import randome and re
import random
import re


#defining the function to be called        
def spin_the_wheel(list1):
    pointer=random.randint(0,20)
    return list1[pointer]
  
    
#define main 
def main():
    
    #defining the lists and opening the file.
    file1 = open('phrases.txt', 'r')
    Lines = file1.readlines()
    count = 0
    phrases=[]
    phrases1=[]
    
    #defining the wheel's values
    wheel=[500,500,500,500,500,550,600,600,600,'BANKRUPT',600,650,650,650,700,'BANKRUPT',700,700,800,900,2500]
    
    for line in Lines:
        p=[]
        p1=[]
        r=list('BCDFGHJKLMNPQRSTVWXYZAEIOUabcdefghijklmnopqrstuvwxyz')
        for i in (line.strip()):
            
            if(i in r):
                p.append((i.upper()))
                p1.append('_')
            
            else: 
                p.append(i)
                p1.append(i)
        phrases.append(p)
        phrases1.append(p1)    
    
    round=1;
    amount=0;
    
    p_counter=random.randint(0,len(phrases)-1)
    phr=phrases[p_counter]
    phr1=phrases1[p_counter]

    
    result=list('BCDFGHJKLMNPQRSTVWXYZ')
    vowels=['A','E','I','O','U']
    
    while(1==1):
    
        print(':::::::::::::::::::::::::::::::::::::::::: ROUND {} of 4 ::'.format(round))
        print('::'+f"{''.join(phr1).center(54)}"+'::')
        print(58*':')
        print('::'+f"{''.join(result).center(27)}"+'::'+f"{''.join(vowels).center(11)}"+'::'+'{:>11}'.format('$'+f"{amount:,}")+' ::')
        print(58*':')
        
        ch='5'      
        while (1==1):
            print('What would you like to do?')
            print('  1 - Spin the wheel')
            print('  2 - Buy a vowel')
            print('  3 - Solve the puzzle')
            print('  4 - Quit the game')

            ch=(input('Enter the number of your choice: '))
            
            if (ch in ['1','2','3','4']): 
                break
            else:
                print('{} is an invalid choice.'.format(ch)) 
    
        if ch=='1':

            pointer = spin_the_wheel(wheel);
            print(pointer)

            if pointer=='BANKRUPT':
                    amount=0;
                    print('The wheel landed on '+str(pointer)+'.')   
            else:
                amount=amount+pointer;
                print('The wheel landed on $'+str(pointer)+".") 
                flag='true'  

                while(flag=='true'):
                  
                    cons=input('Pick a consonant: ')
                    cons=cons.upper()
                    #print(cons)
                    v1=['A','E','I','O','U']
                    if(cons in v1):
                        print('Vowels must be purchased.')
                    elif(cons.isnumeric()):
                        print('The character {} is not a letter.'.format(cons))
                    elif(len(cons) > 1):
                        print('Please enter exactly one character.')
                    elif(cons not in phr):
                        print("I'm sorry, there are no {}'s.".format(cons))
                        flag='false'
                        for i in range(0, len(result)):
                            if(result[i] == cons):
                                result[i]=' ' 
              
                    elif(cons in phr):
                        if (cons in result):
                     #       print(''.join(phr))
                      #      print(len(phr))
                            for i in range(0, len(phr)):
                       #         print(phr[i]+' '+cons)  
                                if phr[i] == cons:
                                    phr1[i] = cons
                            for i in range(0, len(result)):
                                if(result[i] == cons):
                                    result[i]=' '
                        else:
                            print('The letter {} has already been used.'.format(cons))
              
                        flag='false'
                          
                          
                            
                    else:
                        print('no option'+cons)
        elif ch=='2':
            if (amount > 250):
                v=input('Pick a vowel: ')
                v=v.upper()
                cnt=0; 
              
                amount= amount -250
                if (v in vowels):
                    for i in range(0, len(phr)):
                           # print(phr[i]+' '+cons) 
                             
                            if phr[i] == v:
                                phr1[i] = v
                                cnt=cnt+1 
                            
                    for i in range(0, len(vowels)):
                        if(vowels[i] == v):
                            vowels[i]=' '
              
                    if (cnt>0):
                        print('There are '+str(cnt)+v+"'s.")
                else:
                    print("I'm sorry, there are no "+v+"'s.")
            else:
                print('You must have at least $250 to buy a vowel.')
              
        elif ch=='3':    
            guess=8
            phrg=list(phr)
            for i in range(0,guess):
                ritn=random.randint(0,len(phr)-1)
                phrg[ritn]='_'
            
            clue=''.join(phrg)
            print('Clues: '+clue)
            ans=input('Guess: ')
            ans=ans.upper()
            actual=''.join(phr)
            if (ans==actual):
                print('Ladies and gentlemen, we have a winner!')
                print('You earned $'+str(amount)+ 'this round.')
            else:
                round=round+1
                                
        elif ch=='4':
            file1.close()
            break
        
                                
        else:
            print('{} is an invalid choice.'.format(ch))                   
              
#call main         
if __name__ == '__main__':
    main()