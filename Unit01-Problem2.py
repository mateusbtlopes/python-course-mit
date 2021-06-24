# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 20:29:44 2021

@author: mateus.lopes

Problem 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

s = "azcbobobegghakl"
x = 0
y = 3
vowels = 0
caracteres = len(s)

for x in range (caracteres):
   
    if(str(s[x:y]) == "bob"):
        vowels = vowels + 1
        x = x + 1
        y = y + 1

    else:
        y = y + 1

print('Number of times bob occurs is:', vowels)