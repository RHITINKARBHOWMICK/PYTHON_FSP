a=[]
b=[]
for i in range(5):
    x=int(input())
    a.append(x)
for i in a:
    if i not in b:
        b.append(i)
print(b)        
