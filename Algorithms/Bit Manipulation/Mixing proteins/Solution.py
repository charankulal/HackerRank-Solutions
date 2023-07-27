#!/bin/python3

import math
import os
import random
import re
import sys

c2i = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
i2c = ['A', 'B', 'C', 'D']

n, k = [int(x) for x in input().strip().split()]

s = [c2i[x] for x in input().strip()]
s = [s, [0] * len(s)]

a, b = 1, 0

while k > 0:
    a ^= b
    b ^= a
    a ^= b
    
    cp2 = 1
    for i in range(29, 0, -1):
        if k - (1 << i) >= 0:
            cp2 = 1 << i
            break
            
    k -= cp2
    
    for i in range(n):
        s[b][i] = s[a][i] ^ s[a][(i + cp2) % n]
        

for i in s[b]:
    sys.stdout.write(i2c[i])
    
sys.stdout.flush()
