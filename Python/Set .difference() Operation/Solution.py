n=int(input())
int_list=map(int,input().split())
A=set(int_list)
n=int(input())
int_list=map(int,input().split())
B=set(int_list)

print(len(A.difference(B)))
