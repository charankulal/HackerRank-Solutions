m = int(input())
set1 = set(list(map(int, input().split())))
n = int(input())
set2 = set(list(map(int, input().split())))

n1 = set1.difference(set2)
n2 = set2.difference(set1)
L = [str(x) for x in n1] + [str(x) for x in n2]
L.sort(key = int)

print ('\n'.join(L))
