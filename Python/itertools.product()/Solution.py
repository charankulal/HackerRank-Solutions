# Question Link : https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Python 3

import itertools
list_A = map(int, input().split())
list_B = map(int, input().split())
main_list = [list_A, list_B]
cartesian_product = list(itertools.product(*main_list))
print(*cartesian_product, sep=" ")
