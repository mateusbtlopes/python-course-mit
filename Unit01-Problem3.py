# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 21:27:05 2021

@author: mateus.lopes

Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
occur in alphabetical order. For example, if s = 'azcbobobegghakl',
then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd',
then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem,
we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break
and cleared your head.

"""

s = "azcbobobegghakl"
longest = s[0]
current = s[0]

for c in s[1:]:
    if c >= current[-1]:
        current += c
        if len(current) > len(longest):
            longest = current
    else:
        current = c

print ("Longest substring in alphabetical order is:", longest)