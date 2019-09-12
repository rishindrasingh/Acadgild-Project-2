# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 16:40:03 2019

@author: Rishindra
"""

def reverse(s): 
    return s[::-1] 
  
def ispalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False
  
  