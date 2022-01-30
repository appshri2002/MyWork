################################################################################
# Author: Apoorva Shrivastava
# Date: 4/26/2021
# Description
'''
In this prgoram we revoke and provide privlages to a user whilst printing their
information. We have two class. One called Privilages and the other called User.
We revoke and add privlages for a user named Alice. 
'''
################################################################################

#create a class called Privlages
class Privileges:
    
    #initiate parameters.
    def __init__(self, privs="interact,post"):
        self.privs=privs
    
    
    #define methods
        
    def grant(self,prv):
        self.privs.append(prv)
        print("Granted "+prv)
        
    def revoke(self,prv):
        self.privs.remove(prv)
        print("Revoked "+prv)
        
    def get_privs(self):
        return(sorted(self.privs))
#define the class User    
class User:
    
    
    #initiate parameters
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.privs=Privileges()
    
       
    def describe_user(self):
        
        print("User Profile")
        print("  Name: "+self.name)
        print("  Email: "+self.email)
        l=sorted((self.privs.get_privs()))
        print("  Privileges:",self.privs)
        b=""
        
        '''for i in range(0,len(l)):
            if i==0:
                
                b=l[i]
            else:
                b=b+", "+l[i]
                
        print("  Privs:"+b)'''
        
      

        
        
        
        

        
#define main function    
def main():
    
    #call the class and methods
    
    l=["interact","post"]
    
    P=Privileges(l)
    U=User("Alice","alice@example.com")
    U.describe_user()
    P.grant("teleport")
    
   
    
    U.describe_user()
    P.revoke("post")
    
    U.describe_user()
    
    
    

#recall main
if __name__ == '__main__':
    main()
