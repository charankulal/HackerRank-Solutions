# Enter your code here. Read input from STDIN. Print output to STDOUT
s = sorted(input())
lower = list(filter(lambda x: x.islower(),s))
upper = list(filter(lambda x: x.isupper(),s))
odd = list(filter(lambda x: x.isdigit() and int(x)%2 ==1, s))
even = list (filter(lambda x: x.isdigit() and int(x)%2 ==0,s))
print(*(lower + upper+odd+even), sep = "")
