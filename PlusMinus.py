
#https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-week-day-one
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    countpositive=0
    countnegative=0
    countzero=0
    for i in arr:
        if i>0:
            countpositive+=1
        if i<0:
            countnegative+=1
        if i==0:
            countzero+=1
            
    print('%.6f' %(countpositive/len(arr)  )) 
    print('%.6f' %(countnegative/len(arr)  )) 
    print('%.6f' %(countzero/len(arr)  )) 
        
                           
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
