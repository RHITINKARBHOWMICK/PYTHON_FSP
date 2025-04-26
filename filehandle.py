f=open('aec.text','r')
x=f.read()
print(x)
f.close()
f=open('top.py','w')
f.write(x)
f.close()
import top
       
