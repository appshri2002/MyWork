################################################################################
# Author: Apoorva Shrivastava
# Date: 4/26/2021
# Description
'''
In this program we mimic a bank by giving showing the transactions that occured.
We created two classes. One named Account (parent) and the the other named Savings
(child). In account we created the methods deposite, withdraw, and get_balance.
In Savings we called the mentioned methods and added an aditonal method. The additional
methods is called accured_interest.

'''
################################################################################

#create class called account
class Account:

    #initialize parameters
    def __init__(self,balance):

        self.balance= balance
        print('New account balance: $'+format(balance,'.2f'))

    #define method named deposite where money is deposited and printed
    def deposit(self,amount):
        self.balance+=amount
        print('Deposit: $'+format(amount,'.2f'))


    #define method withdraw where money is withdrawed
    def withdraw(self,amount):

        print('Withdraw: $'+format(amount,'.2f'))


        if (amount>self.balance):
            print('Insufficient funds. Withdrawal canceled.')
        else:
            self.balance=self.balance-amount


    #define method get_balance where the balance is printed
    def get_balance(self):

        print('Balance: $'+format(self.balance,'.2f'))


#child class called Savings
class Savings(Account):

    #initializ parameter
    def __init__(self,balance,interest_rate):


        self.interest_rate= interest_rate

        Account.__init__(self, balance,interest_rate)



    def accure_interest(self):



        interest_rate= self.balance* (self.interest_rate/100)

        self.balance=self.balance+interest_rate

        print('Interest payment: $'+format(interest_rate,'.2f'))


#define main method
def main():

    A=Savings(200,10)
    A.get_balance()
    A.deposit(12.34)
    A.get_balance()
    A.withdraw(40)
    A.get_balance()
    A.withdraw(200)
    A.get_balance()
    A.accure_interest()
    A.accure_interest()
    A.accure_interest()
    A.withdraw(200)
    A.get_balance()


#call main function
if __name__ == '__main__':
    main()
