# Question Link: https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy

N=int(input())

listA=[list(map(int,input().split())) for i in range(N)]
listB=[list(map(int,input().split())) for i in range(N)]

A=numpy.array(listA)
B=numpy.array(listB)

print(numpy.dot(A,B))
