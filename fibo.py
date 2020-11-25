# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 21:59:44 2020

@author: aksha
"""
def fib(n):
    sum = 0
    if n == 1 or n == 0:
        sum +=1
    else:
        sum += fib(n-2) + fib(n-1)
    return sum

if __name__ == "__main__":
    n = int(input("Enter the number whose fibonacci series you want to find = "))
    s = fib(n)
    print(f"Fibonacci is = {s}")
