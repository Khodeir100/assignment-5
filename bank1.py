# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:40:20 2024

@author: HiTech
"""

class bank():
    users=["mohamed","ali","ibrahim"]
    accounts={"mohamed":["1234",100],"ali":["0000",200],"ibrahim":["5678",300]}
    bank_account=[]
    def registration(self):
        self.user=str(input("enter a username "))
        self.password=str(input("enter a password"))
        if self.user in bank.users:
            print("this username already exist")
        else:
            bank.accounts[self.user]=[self.password,0]
        return bank.accounts
    def login(self):
        self.user=str(input("enter your username "))
        if self.user in bank.users:
            self.account=bank.accounts[self.user]
            self.password=str(input("enter your password"))
            if self.password == self.account[0]:
                print("logged in successfully")
                bank.bank_account=self.account
                return bank.bank_account
            else:
                print("password is not correct")   
        else:
            print("username does not exist")
    def check_balance(self):
        if bank.bank_account == []:
            pass
        else:
            print(f"your account balance is {bank.bank_account[1]}")
    def deposit(self):
       if bank.bank_account == []:
           pass
       else:
           self.deposit_amount = abs(int(input("enter the amount of depsition")))
           bank.bank_account[1] = bank.bank_account[1] + self.deposit_amount
           bank.accounts[self.user]=bank.bank_account
           print(f"your new account balance is {bank.bank_account[1]}")
           return bank.bank_account and bank.accounts
    def withdrawl(self):
        if bank.bank_account == []:
           pass
        else:
           self.withdrawl_amount = abs(int(input("enter the withdrawl amount")))
           bank.bank_account[1] = bank.bank_account[1] - self.withdrawl_amount
           bank.accounts[self.user]=bank.bank_account
           print(f"your new account balance is {bank.bank_account[1]}")
           return bank.bank_account and bank.accounts
