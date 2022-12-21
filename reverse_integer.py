# this function reverses the integer number

import numpy as np
def reverse_integer():
    n = str(input())
    
    if int(n) < 0:
        print(f'-{int(n[:0:-1])}')
    elif int(n) > 0:
        print( n[::-1])
    
if __name__ == '__main__':
    reverse_integer()
