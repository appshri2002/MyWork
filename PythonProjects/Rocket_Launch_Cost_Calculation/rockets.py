################################################################################
# Author: Apoorva Shrivastava
# Date: 4/26/2021
# Description 
'''
In this program we we calculate the total cost per launch for 5 different rockets.
This program has a class called Rocket and a reusable class called ReusableRocket.
We created a method in both of the class called cost_per_launch where we calculate 
the total cost. 
'''
################################################################################


#create a class called Rocket
class Rocket:
     
     #initialize parameters
     def __init__(self, name,booster_cost,upper_stage_cost,fuel_cost):
          self.name= name
          self.booster_cost= booster_cost
          self.upper_stage_cost= upper_stage_cost
          self.fuel_cost= fuel_cost
          
     #create method to calculate the total cost for each launch     
     def cost_per_launch(self):
          reusable_cost_per_launch = self.booster_cost + self.upper_stage_cost + self.fuel_cost
          print("This "+self.name+' cost $'+str(reusable_cost_per_launch),'million per launch.')

#Create a reusable class called ReusableRocket that uses a class called Rocket as an inheritance.          
class ReusableRocket(Rocket):
     
     #initialize parameter
     def __init__(self, name, booster_cost, upper_stage_cost, fuel_cost,uses):

          Rocket.__init__(self, name, booster_cost, upper_stage_cost, fuel_cost)
          
          self.uses=uses
          
     #overiding the cost per launch method from the parent class called Rocket     
     def cost_per_launch(self):
          reusable_cost_per_launch = (self.booster_cost/self.uses) + self.upper_stage_cost + self.fuel_cost
          print("This "+self.name+' cost $'+str(reusable_cost_per_launch),'million per launch.')
          
          

     
#define main function    
def main():
     
     #create an object from the class ReusableRocket
     
     A=ReusableRocket("Atlas V",65.4,42.6,0.23,1)
     A.cost_per_launch()
     
     A=ReusableRocket("Ariane 5",83.5,55.6,0.69,1)
     A.cost_per_launch()  
     
     A=ReusableRocket("Long March 3B",28.5,19.0,2.38,1)
     A.cost_per_launch()     
     
     A=ReusableRocket("Soyuz 2",20.9,13.9,0.24,1)
     A.cost_per_launch()     
     
     A=ReusableRocket("Falcon 9",43.0,18.6,0.45,10)
     A.cost_per_launch()     



#call main

if __name__ == '__main__':
    main()
