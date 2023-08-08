# Enter your code here. Read input from STDIN. Print output to STDOUT
_, en_subscribers = input(), set(map(int, input().split())) 
_, fr_subscribers = input(), set(map(int, input().split())) 
print(len(en_subscribers.union(fr_subscribers)))
