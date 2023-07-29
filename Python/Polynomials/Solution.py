#Question Link: https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy

P = list(map(float,input().split()));
x = input();
print(numpy.polyval(P,int(x)));
