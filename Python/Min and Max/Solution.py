# Question Link : https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy
N,M = map(int,input().split())

lista=[list(map(int,input().split())) for i in range(N)]

ar=numpy.array(lista)

print(max(numpy.min(ar,axis=1)))   


