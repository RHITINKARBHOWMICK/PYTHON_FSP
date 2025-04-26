try:
    import calc
    a=int(input("enter the first number :"))
    b=int(input("enter the second number:"))
    calc.add(a,b)
    calc.sub(a,b)
    calc.mult(a,b)
    calc.div(a,b)               
except ValueError:
       print("value error occured")
except ZeroDivisionError:
        print("zero division error occured.provide number greater than zero")
except KeyboardInterrupt :
             print('user interuppted during input')
               
