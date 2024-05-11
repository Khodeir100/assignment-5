# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:42:06 2024

@author: HiTech
"""

from bank1 import bank
a=bank()
option=input(''' 
             press L for login
             if you don't have an account press R for registration
             ''')
if option == "L":
    a.login()
    if a.bank_account != []:
        while True:
            options=input(''' Check balance ... press C
                      Deposit ... press D
                      Withdrawl ... press W
                      Exit ... N
                      ''')
            if options == "C":
                a.check_balance()
            elif options == "D":
                a.deposit()
            elif options == "W":
                a.withdrawl()
            elif options == "N":
                print ("thank you")
            else:
                print("invalid input")
            break
    else:
        pass
elif option == "R":
    a.registration()
else:
    print("invalid input")