    # take input and check 3 digit numbers or not  then reverse it and check if palindrome number or not
list=[]
for i in range(5):
    while True:
    x=int(input())
    if len(x)>2:
        list.append(x)
        break
list.reverse()

         
