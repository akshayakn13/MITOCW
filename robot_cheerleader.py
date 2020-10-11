# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 07:57:09 2020

@author: aksha
"""

word = input("I will cheer for you enter a word ")
times = int(input("Enter your enthusiasm level "))

an_letters = "aefhilmnorsxAEFHILMNORSX"

for char in word:
    if char in an_letters:
        print("Give me an " + char + "! "+ char.upper())
        print("#"*50)
    else:
        print("Give me a " + char + "! "+ char.upper())
        print("#"*50)
print("WHat does that it spell !!!!!!!")
for i in range(times):
    print(word)