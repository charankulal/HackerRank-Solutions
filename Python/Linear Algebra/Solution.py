# Question Link : https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy

N=int(input())
lista=[list(map(float,input().split())) for i in range(N)]
numpy.set_printoptions(legacy='1.13')
print(numpy.linalg.det(lista))

