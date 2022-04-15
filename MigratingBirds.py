#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    """
    length=len(arr)
    count=0
    sum=0
    for i in range(length):
        j=i+1
        while j<length:
            if(arr[i]==arr[j]):
                count+=1
                sum=arr[i]
            j+=1
    return sum
    """
    count = [0]*6
    for i in arr:
        count[i]+=1
    return count.index(max(count))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
