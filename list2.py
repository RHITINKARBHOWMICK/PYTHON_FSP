#print a list by user and print first 3 values
list=[]
for i in range(10):
    i=int(input())
    list.append(i)
    list.sort(reverse=True)
print(list[:3])    
