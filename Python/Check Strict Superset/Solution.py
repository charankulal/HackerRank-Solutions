A = set(input().split())
N = int(input())
print(all(A > set(input().split())  for _ in range(N)))
