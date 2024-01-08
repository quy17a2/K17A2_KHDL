x = int(input("Nhập vào một số nguyên X: "))
S = 1 + x + (x**3) / 3 + (x**5) / 5
print(f"Giá trị của biểu thức S với x = {x} là: {S}")
#7.2
result=1+2
print('result =',result)
original_result =result
result = result - 1

print('result =',result)
original_result = result
result = result * 2
original_result = result
print('result =',result)
result = result ** 3
original_result = result
print('result =',result)
result = result + 8
original_result = result
print('result =',result)
result = result % 7
original_result = result
print('result =',result)
result = result // 2
original_result = result
print('result =', result)
#7.3
result = 5
print('result =',result)
result -= 1
print ('result =',result)
result += 3
print('result =',result)
result = - result 
print('resule =',result)
result = True
print('not result=',not result)
#7.4
x=10
y=4
print('x = %d, y= %d'%(x,y))
equivelence =x==y
print('x==y is',equivelence)
equivelence = x!=y
print('x!=y is',equivelence)
equivelence =x>y
print('x>y is',equivelence)
x=8
y=9
print('x =%d,y =%d'%(x,y))
equivelence = x>= y
print('x>=y is',equivelence)
equivelence = x<y
print('x<y is',equivelence)
equivelence = x<=y
print('x<=y is',equivelence) 
#7.5
x=15
y=12
print('binary of x',bin(x), ',binary of y =',bin(y))
print('x & y =',bin(x & y))
print('x / y =',bin(x | y))
print('x ^ y =',bin(x^y))
print('~x =',bin(~x))
print('x << 2 =',bin(x << 2))
print('y >> 2 =',bin(y >> 2))
#7.6
x= True
Y=False
print('x and y :',x and y)
print('x or y :',x or y)
print('not x :',not x)
print('x is y :', x is y)
print(' x is not y :',x is not Y)




