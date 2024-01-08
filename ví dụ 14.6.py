try:
    x=eval(input("nhập x\n"))
    y=eval(input("nhập y\n"))
    z=x/y
except (NameError,ZeroDivisionError)as er:
    print('Error :',er)

else:
    print('x/y',z)
finally:
    print('x+y =',x+y)
    print('x-y =',x-y)
    print('x*y =',x*y)
    