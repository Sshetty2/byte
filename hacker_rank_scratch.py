# import math
# import os
# import random
# import re
# import sys

# arr = []

# if __name__ == '__main__':
#     tmp = [int(x) for x in str(input()).split(" ")]
#     arr.append(tmp)
# print(arr)

import functools

def calc_avg(arr):
    print(len(arr))
    (functools.reduce(lambda x,y: x+y, arr))/len(arr)

print(calc_avg([100, 80]))