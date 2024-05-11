# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:05:43 2024

@author: HiTech
"""

class library():
    games=["A","B","C"]
    donors={"mohamed":"A","ali":"B","ibrahim":"C"}
    lenders={"ahmed":"D"}
    def game_list(self):
        print(library.games)
    def lend(self):
        self.lender=str(input("enter your name "))
        self.game=str(input("enter the game "))
        library.games.remove(self.game)
        library.lenders[self.lender]=self.game
    def returnb(self):
        self.lendr=str(input("enter your name "))
        self.gam=str(input("enter the game "))
        if self.lendr in library.lenders:
            library.games.append(self.gam)
            library.lenders[self.lendr]=[]
        else:
            print("your name isn't in the lenders data")
    def donate(self):
        self.donor=str(input("enter your name "))
        self.game=str(input("enter the game "))
        library.games.append(self.game)
        library.donors[self.donor]=self.game
        
a=library()
options=str(input(''' to check game list .. press C
                  to lend a game .. press L
                  to return a game .. press R
                  to donat a game .. press D
                  to Exit .. press E
                  '''))
while True:
    if options == "C":
        a.game_list()
    elif options == "L":
        a.lend()
    elif options == "R":
        a.returnb()
    elif options == "D":
        a.donate()
    elif options == "E":
        print("Thank you ")
    else:
        print("invalid input ")
    break