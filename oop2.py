class roman:
    def int_to_roman(self,num):
        if num>3999 or num<1:
            return "input out of range"
        v=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        s=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        rom=' '
        i=0
        while num>0:
            for _ in range (num//v[i]):
                rom+=s[i]
                num -=v[i]
            i+=1
        return rom
print(roman().int_to_roman(1))
print(roman().int_to_roman(3999))
