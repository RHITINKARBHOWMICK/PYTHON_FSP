#greatest between 3 nos.

a=int(input("enter the first number:"))
b=int(input("enter the first number:"))
c=int(input("enter the first number:"))
if a>b:
    if a>c:
        print("a is the greatest:",a)
    else:
        print("c is the greatest:",c)
elif b>c:
        print("b is the greatest",b)
else:
    print("c is the greatest:",c)
