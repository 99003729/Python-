n=int(input())
c=0
s=set()
while n>c:
    name=input()
    s.add(name)
    c+=1
count=len(s)
print(count)