#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sum=0
    length=len(arr)
    for i in range(length):
        sum+=arr[i]
    print(sum-max(arr) ,sum-min(arr))
            

if __name__ == '__main__':

    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
