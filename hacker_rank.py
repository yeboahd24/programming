

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print('Weird')
    if n > 20  and n % 2 == 0:
        print('Not Weird')

    numBer = range(2, 5)
    if n % 2 == 0 and n in numBer:
        print('Not Weird')

    upper = range(6, 21)
    if n % 2 == 0 and n in upper:
 	  	print('Weird')
