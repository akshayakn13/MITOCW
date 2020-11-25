# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:49:21 2020

@author: aksha
"""

def move_statement(to,fro):
    """
    

    Parameters
    ----------
    to : integer
        destination of moving spikes
    fro : integer
        origination of spikes.

    Returns
    -------
    None.

    """
    print(f"moving from tower {str(to)} to tower {str(fro)}")

def towers(n,to,fro,spare):
    """
    Implementation of tower of hanoi:
    Parameters
    ---------
    n : number of spikes
    to : destination of moving spikes
    fro : origination of spikes.
    spare : 3rd tower

    Returns
    -------
    None.
    """
    if n==1:
        move_statement(to, fro)
    else:
        towers(n-1,to,spare,fro)
        towers(1,to,fro,spare)
        towers(n-1,spare,fro,to)
        
        
if __name__=="__main__":
    to = int(input("Enter origination tower ="))
    fro = int(input("Enter destination tower ="))
    spare = int(input("Enter spare tower ="))
    n = int(input("Enter number of spikes ="))
    towers(n,to,fro,spare)