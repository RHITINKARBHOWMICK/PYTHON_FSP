def rhitinkar(st,sp=None,se=1):
    if sp is None:
        sp=st
        st=0
    if se==0:
        raise  ValueError("zero given")
    if se >0:
        while st <sp:
            yield st
            st+=se
    else:
        while st>sp:
            yield st
            st +=se
for i in rhitinkar(10,0,-1):
    print(i)
