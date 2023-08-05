# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 

for _ in range(int(input())):
    str_ = input()
    str_ = re.sub(r"(?<= )(&&)(?= )", "and", str_)
    print(re.sub(r"(?<= )(\|\|)(?= )", "or", str_))
