# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 16:19:42 2019

@author: Rishindra
"""


def fib2(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return fib2(n-1)+fib2(n-2) 
  
  
