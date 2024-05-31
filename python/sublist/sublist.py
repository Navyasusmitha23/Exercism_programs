"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST =   'SUBLIST'
EQUAL =     'EQUAL'
SUPERLIST = 'SUPERLIST'
UNEQUAL =   'UNEQUAL'

def sublist(list_one, list_two):
    len1,len2 = len(list_one),len(list_two)
    if len1 == len2:
       if list_one == list_two:
          return 'EQUAL'
    elif len1<len2:
         for i in range(len2-len1+1):
             if list_two[i:i+len1] == list_one:
                return 'SUBLIST'
    else: 
         for i in range(len1-len2+1):
             if list_one[i:i+len2] == list_two:
                return 'SUPERLIST'
        
    return UNEQUAL
      
