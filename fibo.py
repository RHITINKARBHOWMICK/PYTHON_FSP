c=int(input("enter the range: "))
a,b=0,1
print(a,b,end=" ")#end holds the cursor in the same line
for i in range(c):
    c=a+b
    print(c,end=" ")
    a,b=b,c
