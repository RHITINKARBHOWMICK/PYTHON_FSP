#slicing method
a="12345"
for i in range(1,6):
    print(" "*(5-i)+a[0:i-1]+a[i-1::-1])
