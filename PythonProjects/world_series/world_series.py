################################################################################
# Author:Apoorva Shrivastava
# Date:4/12/2021
# Description ...
'''here we load a file and put the data in a dictionary
we then call that function later and present it based on the users
input
'''
################################################################################

#def function
    
def load_winners_data():
    
    
    #create dict and assign values to variables
    winner={}
    year=1903
    teams={}
    test=" "
    
    
    #open file
    with open("WorldSeriesWinners.txt") as fo:
        
        
        
        #code for dict
        for team in fo:
            
            teamname=team.strip()
            
            if year==1904 or year==1994:
                year+=1
                #winner.update({year:test})
                #continue
              
                
                
            
            
            winner.update({year:teamname})
            year+=1        
        
        
            if teamname in teams:
                val=teams[teamname]
                teams.update({teamname:val+1})
            else:
                teams.update({teamname:1})
           
    ls=(teams,winner)
    
    
    
   #return list
    return ls
 
    
#def main fucntion
def main():
    
    
    #call function
    result=load_winners_data()
    years=result[1]
    t=result[0]
    
    
    #ask user for input
    year_inp= int(input("Enter a year in the range 1903 -- 2020: ")) 
    
    if year_inp==1994 or year_inp==1904:
        print("The World Series wasn't played in the year "+str(year_inp)+".")
    
    elif 1903<=year_inp<=2020:
        
    
        wt=years[year_inp]
        now=t[wt]
    

        print("The "+wt+" won the World Series in "+str(year_inp)+"." )
        print("They have won the World Series",now,"times.")
        
    else:
        print("Data for the year",year_inp,"is not included in this system.")
        
 #call main   
if __name__ == '__main__':
    main()
