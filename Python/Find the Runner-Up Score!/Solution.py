# Question LInk : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

# Python 3


n = int(input())
arr = map(int, input().split())
arr=list(arr)
x = max(arr)
y = -9999999
for i in range(0,n):
    if arr[i]<x and arr[i] > y:
        y = arr[i]
    
print(y)
