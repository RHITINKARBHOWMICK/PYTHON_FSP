#create a list by taking value from the user then print odd numbers

list=[]
for i in range(10):
    i=int(input())
    list.append(i)
odd=[]
for n in list:
    if n%2!=0:
        print(n)
# by list comprehension method
odd=[n for n in list if n%2!=0]
print(odd)


