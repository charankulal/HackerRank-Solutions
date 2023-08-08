# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def valid_uid(uid):
    if len(re.findall(r"[A-Z]", uid)) < 2 or \
            len(re.findall(r"[0-9]", uid)) < 3 or \
            not re.match(r"[A-Za-z0-9]{10}$", uid) or \
            len(set(uid)) != len(uid):
        return False
    
    return True
    
n = int(input())
for _ in range(n):
    uid = input()
    if valid_uid(uid):
        print("Valid")
    else:
        print("Invalid")
