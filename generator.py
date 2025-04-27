def mygen(l):
    n=0
    while n<l:
        yield n
        n+=1
ngen=mygen(5)
for i in ngen:
    print(i)
        
