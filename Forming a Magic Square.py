#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

        
def is_magic(square):
    Ktra_khong_trung =[]
    for i in range(3):
        for j in range(3):
            Ktra_khong_trung.append(square[i][j])
            if (square[i][j]<=0) or (square[i][j]>=10):
                return False
        if sum(square[i][:]) != 15:
            return False
        if sum(square[:][i]) != 15:
            return False
        if square[0][0]+square[1][1]+square[2][2] != 15:
            return False
        if square[0][2]+square[1][1]+square[2][0] != 15:
            return False
        if len(Ktra_khong_trung) != len(set(Ktra_khong_trung)):
            return False
    return True
    
def formingMagicSquare(s):
    # Write your code here
    a_square = [[0, 0, 0], [0, 5, 0], [0, 0, 0]]
    list_cost = []
    for i in range(1,10):
        a_square = [[0, 0, 0], [0, 5, 0], [0, 0, 0]]
        if i == 5:
            continue
        a_square[0][0] = i
        a_square[2][2] = 10-i
        for j in range(1,10):
            if (j == 5) or (j == i):
                continue
            a_square[0][1] = j
            a_square[0][2] = 15-a_square[0][1]-a_square[0][0]
            a_square[1][2] = 15-a_square[0][2]-a_square[2][2]
            a_square[1][0] = 10-a_square[1][2]
            a_square[2][1] = 10-a_square[0][1]
            a_square[2][0] = 10-a_square[0][2]
            if is_magic(a_square) == True:
                cost = 0
                for m in range(3):
                    for n in range(3):
                        cost += abs(a_square[m][n]-s[m][n])  
                list_cost.append(cost)
    return min(list_cost)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
