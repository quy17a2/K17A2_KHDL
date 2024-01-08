print("Bài toán tìm số lớn nhất và nhỏ nhất.")

a=eval(input("Nhập số a:"))

b=eval(input("Nhập số b:"))

c=eval(input("Nhập số c:"))

d=eval(input("Nhập số d:"))

g=0

h=0

while(g<a)or(g<b)or(g<c)or(g<d):

    g+=1

h=g

while(h>a)or(h>b)or(h>c)or(h>c):

    h-=1

print("max =",g)

print("min =",h)        
8.2
a=eval(input("Nhập số:"))

print("Giá trị tuyệt đối của",a,"là:","|",a,"|=",abs(a))

#8.3
print("Giải phương trình ax+b=0")

a = int(input("Nhập số a:"))

b = int(input("Nhập số b:"))

if a == 0:

    if b == 0:

        print("Phương trình vô số nghiệm.")

    else: print("Phương trình vô nghiệm.") 

else: 

    print('Nghiệm của phương trình là: x = ', -b/a)
#8.4
a = eval(input("nhap do dai canh a: "))

b = eval(input("nhap do dai canh b: "))

c = eval(input("nhap do dai canh c: "))

if a+b<c and b+c<b:

    print("day khong phai la tam giac")

else:

    print("day la mot tam giac")

    import math

    p=(a+b+c)/2

    S= math.sqrt(p*(p-a)*(p-b)*(p-c))

    print("Dien tich tam giac tren la: ",S)
    #8.5
    a = int(input("Nhập năm: "))

if ((a%4==0) and (a%100!=0) or (a%400==0)):

    print("năm", a, "là năm nhuận")

else:

    print("năm", a, "không phải là năm nhuận")
#8.6
loai_xe=int(input("Cho biết loại xe là 4/7 ?"))
so_km=float(input("Nhập số km chạy bằng = "))
time_cho=float(input("Cho biết thời gian chờ (phút chờ) = "))
tien_cuoc=float(0)
tien_di_chuyen=float(0)
if time_cho >=5:
    tien_cho=(time_cho-5)*0.8
else:
    tien_cho=0
if loai_xe==4:
    if so_km <=0.8:
        tien_di_chuyen=0.8*11000
    elif so_km <=20:
        tien_di_chuyen=0.8*11000+(20-so_km)*12100
    else:
        tien_di_chuyen=0.8*11000+(20-0.8)*12100+(so_km-20)*10000
    tien_cuoc=tien_cho+tien_di_chuyen
    print("Cước phí xe taxi 4 chỗ của quý khách là %0.2f"%tien_cuoc)
if loai_xe==7:
    if so_km <=0.8:
        tien_cuoc+tien_cho+0.8*13000
    elif so_km <=30:
        tien_cuoc=tien_cho+0.8*13000+(30-so_km)*14100
    else:
        tien_cuoc=tien_cho+0.8*13000+(30-0.8)*14100+(so_km-30)*12000
    tien_cuoc=tien_cho+tien_di_chuyen
    print("Cước phí xe taxi 7 chỗ của quý khách là %0.2f"%tien_cuoc)
#8.7
a=eval(input("Nhập số KWh tiêu thụ:"))
if a>=0:
    if a<=50:
       print("Tổng số tiền phải trả là:",a*1678,"đồng.")
    elif a<=100:
       print("Tổng số tiền phải trả là:",50*1678+(a-50)*1734,"đồng.")
    elif a<=200:
       print("Tổng số tiền phải trả là:",50*(1678+1734)+(a-100)*2014,"đồng.")
    elif a<=300:
       print("Tổng số tiền phải trả là:",50*(1678+1734+2014)+(a-200)*2536,"đồng.")
    elif a<=400:
       print("Tổng số tiền phải trả là:",50*(1678+1734+2014+2536)+(a-300)*2834,"đồng.")
    else:
       print("Tổng số tiền phải trả là:",50*(1678+1734+2014+2536+2834)+(a-400)*2927,"đồng.")     
else:
   print("Số KWh không hợp lệ.")
   

    