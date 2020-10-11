# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:29:55 2020

@author: aksha
"""

import random
# print(x)
# play = input("enter y to play again n to quit:")
def sim(x):
    if x ==1:
        print(" _______")
        print("|       |")
        print("|   *   |")
        print("|       |")
        print(" -------")
    if x ==2:
        print(" _______")
        print("|       |")
        print("|  * *  |")
        print("|       |")
        print(" -------")
    if x ==3:
        print(" _______")
        print("|      *|")
        print("|   *   |")
        print("| *     |")
        print(" -------")
    if x ==4:
        print(" _______")
        print("|*    *|")
        print("|      |")
        print("|*    *|")
        print(" -------")
    if x ==5:
        print(" _______")
        print("|*     *|")
        print("|   *  |")
        print("|*     *|")
        print(" -------")
    if x ==6:
        print(" _______")
        print("|*  *  *|")
        print("|       |")
        print("|       |")
        print("|*  *  *|")
        print(" -------")
if __name__ == '__main__':
    play = input("enter y to play again n to quit:")
    while play == 'y':
        sim(random.randint(1,6))
        play = input("enter y to play again n to quit:")