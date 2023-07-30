# Question LInk :https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Pypy3


import re
T = int(input())
for _ in range(T):
    try:
        re.compile(input())
        print(True)
    except Exception:
        print(False)
