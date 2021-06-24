# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 20:29:44 2021

@author: mateus.lopes

Problem 1

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:
    
Number of vowels: 5
"""

s = "azcbobobegghakl"
x = 0
vowels = 0
caracteres = len(s)

for x in range (caracteres):
    
    if(s[x] == "a" or s[x] == "e" or s[x] == "i" or s[x] == "o" or s[x] == "u"):
        vowels = vowels + 1
        x = x + 1
        
print('Number of vowels:', vowels)