# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())
for _ in range(N):
    pattern = r'^[789]\d{9}$'
    print ( 'YES' if re.match(pattern,input()) else 'NO')
