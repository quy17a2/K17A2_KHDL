r=float(input('nhập bán kính:'))
a=float(input('nhập chiều dài:'))
b=float(input('nhập chiều rộng:'))
s=lambda r:3.14*(r**2)
p=lambda r:3.14*2*r
S=lambda a,b:a*b
P=lambda a,b:(a+b)*2
print('diện tích hình tròn:',s(r))
print('chu vi hình tròn:',p(r))
print('diện tích hình chữ nhật:',S(a,b))
print('chu vi hình chữ nhật:',P(a,b))