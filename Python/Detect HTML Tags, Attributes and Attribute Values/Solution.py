# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag, attrs):
        print(tag)
        for i in attrs:
            print("->",i[0],">",i[1])
        
    def handle_startendtag(self,tag, attrs):
        print(tag)
        for i in attrs:
            print("->",i[0],">",i[1])


N=int(input())
tmp=""
for _ in range(N):
    tmp=tmp+input()+"\n"
    

    
psr=MyHTMLParser()
psr.feed(tmp)
