#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    lst=s.split(':')
   
    hours=lst[0]
    minutes=str(lst[1])
    temp=lst[2]
    seconds=str(temp[:2])
    status=temp[2:]
    print(lst)
    if status=="AM":
        if hours=="12":
            result_hours="00"
        else:
            result_hours=hours
    else:
        if hours=="12":
            result_hours="12"
        else:
            result_hours=str(int(hours)+12)
    
    result=result_hours + ':' + minutes + ':' + seconds
    return result        
            
                        

    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
