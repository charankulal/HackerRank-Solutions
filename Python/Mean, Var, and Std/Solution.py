# Question Link: https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy

n,m = map(int,input().split())

lista=[list(map(int,input().split())) for i in range(n)]

ar=numpy.array(lista)


print(numpy.mean(ar,axis=1), numpy.var(ar,axis=0), round(numpy.std(ar),11), sep='\n')

