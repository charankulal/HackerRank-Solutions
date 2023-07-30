# Question Link : https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


# Python 3

import itertools

s, k = input().split()

for c in itertools.combinations_with_replacement(sorted(s), int(k)):
    print("".join(c))
