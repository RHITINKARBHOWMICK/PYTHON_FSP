#check first negative or positive then even or odd ..

a=int(input("enter a number :"))
if a<0:
    print("the number is negative:")
    if a%2==0:
        print("the number is even")
    else:
         print("the number is odd")
elif a>0:
    print("the number is positive:")
    if a%2==0:
        print("the number is even") 
    else:
        print("the number is odd:")
    
else:
    print("neutral number")
