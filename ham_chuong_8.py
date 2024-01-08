def chuong8_bai1():

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



def chuong8_bai2():

  a = float(input("Nhap gia tri a:"))

  if a > 0:

    print("|x| = ", a)

  else:

    print("|x| = ", -a)



def chuong8_bai3():

 print("Giải phương trình ax+b=0")

 a = int(input("Nhập số a:"))

 b = int(input("Nhập số b:"))

 if a == 0:

    if b == 0:

        print("Phương trình vô số nghiệm.")

    else: print("Phương trình vô nghiệm.") 

 else: 

    print('Nghiệm của phương trình là: x = ', -b/a)



def chuong8_bai4():

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



def chuong8_bai5():
  year = int(input("Nhap nam can kiem tra: "))
  if year < 1:
    print("Nam khong xac dinh")
  else:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} la nam nhuan")
    else:
        print(f"{year} khong phai la nam nhuan")

def chuong8_bai6():
   loai_xe = int(input("Nhap loai xe 4 cho hoac 7 cho (4,7): "))
   if loai_xe != 4 and loai_xe != 7:
    print("Yeu cau nhap 4 hoac 7")
   else:
    quang_duong = float(input("Nhap quang duong (km): "))
    if quang_duong <=0:
      print("Quang duong khong xac dinh")
    else:
        thoi_gian_cho = int(input("Nhap thoi gian cho (phut): "))
        if thoi_gian_cho < 0:
            print("Thoi gian cho khong xac dinh")
        else:
            tong_tien = 0.0
            tien_cho = 0.0
            if thoi_gian_cho > 5:
                tien_cho = (thoi_gian_cho - 5) * 800
            if loai_xe == 4:
                if quang_duong >= 21:
                    tong_tien = 11000 + (20 - 0.8)*12100 + (quang_duong - 20) * 10000 + tien_cho
                elif quang_duong > 0.8:
                    tong_tien = 11000 + (quang_duong - 0.8)*12100 + tien_cho
                else:
                    tong_tien = 11000 + tien_cho
            if loai_xe == 7:
                if quang_duong >= 21:
                    tong_tien = 13000 + (20 - 0.8)*14100 + (quang_duong - 20) * 12000 + tien_cho
                elif quang_duong > 0.8:
                    tong_tien = 13000 + (quang_duong - 0.8)*14100 + tien_cho
                else:
                    tong_tien = 13000 + tien_cho
            print(f"Loai xe: {loai_xe} cho")
            print(f"Quang duong: {quang_duong} km")
            print(f"Thoi gian cho: {thoi_gian_cho} phut")
            print(f"Tong tien: {tong_tien} VND")

def chuong8_bai7():
   kwh_dien = float(input("Nhap so kWh dien (kWh): "))
   if kwh_dien < 0: 
    print("So kWh khong xac dinh")
   else:
    tong_tien = 0.0
    if kwh_dien >= 401:
        tong_tien = 50*1.675 + 50*1734 + 100*2014 + 100*2536 + 100*2834 + (kwh_dien - 400)*2927
    elif kwh_dien >= 301: 
        tong_tien = 50*1.675 + 50*1734 + 100*2014 + 100*2536 + (kwh_dien - 300)*2834
    elif kwh_dien >= 201: 
        tong_tien = 50*1.675 + 50*1734 + 100*2014 + (kwh_dien - 200)*2536
    elif kwh_dien >= 101: 
        tong_tien = 50*1.675 + 50*1734 + (kwh_dien - 100)*2014
    elif kwh_dien >= 51:
        tong_tien = 50*1.675 + (kwh_dien - 50)*1734
    else: 
        tong_tien = kwh_dien*1.675
    print(f"Tong tiẻn dien la: {tong_tien}")

def chuong8_bai8():
  m_1 = "Standard - 1,260,000" 
  m_2 = "Superior Garden View - 1,550,000" 
  m_3 = "Superior Ocean View - 1,830,000" 
  m_4 = "Garden View Bungalow - 1,830,000" 
  m_5 = "Pool View Bungalow - 2,120,000" 
  m_6 = "Family Room - 2,120,000" 
  m_7 = "Beach Front Bungalow - 2,540,000" 
  m_8 = "VIP sea View - 4,800,000" 
  m = int(input("Nhap ma phong (1 - 8):"))
  if m > 8 and m < 1:
    print("Ma phong khong hop le")
  else:
    so_dem = int(input("Nhap so dem o lai: "))
    if so_dem < 1:
        print("So dem khong hop le")
    else:
        tong_tien = 0.0
        giam_gia = 0.0
        if so_dem > 1 and so_dem < 4:
           giam_gia = 0.25
        elif so_dem >= 4:
            giam_gia = 0.3
        else:
            giam_gia = 0.0
        if m == 1:  
            tong_tien = 1260000*so_dem*(1-giam_gia)
            print(f"Ma {m} - {m_1} - {so_dem} dem - giam {giam_gia*100}%: {tong_tien}")
        if m == 2:
            tong_tien = 1550000*so_dem*(1-giam_gia)
            print(f"Ma {m} - {m_2} - {so_dem} dem - giam {giam_gia*100}%: {tong_tien}")
        if m == 3:
            tong_tien = 1830000*so_dem*(1-giam_gia)
            print(f"Ma {m} - {m_3} - {so_dem} dem - giam {giam_gia*100}%: {tong_tien}")
        if m == 4:
            tong_tien = 1830000*so_dem*(1-giam_gia)
            print(f"Ma {m} - {m_4} - {so_dem} dem - giam {giam_gia*100}%: {tong_tien}")
        if m == 5:
            tong_tien = 2120000*so_dem*(1-giam_gia)
            print(f"Ma {m} - {m_5} - {so_dem} dem - giam {giam_gia*100}%: {tong_tien}")
        if m == 6:
            tong_tien = 2120000*so_dem*(1-giam_gia)
            print(f"Ma {m} - {m_6} - {so_dem} dem - giam {giam_gia*100}%: {tong_tien}")
        if m == 7:
            tong_tien = 2540000*so_dem*(1-giam_gia)
            print(f"Ma {m} - {m_7} - {so_dem} dem - giam {giam_gia*100}%: {tong_tien}")
        if m == 8:
            tong_tien = 4800000*so_dem*(1-giam_gia)
            print(f"Ma {m} - {m_8} - {so_dem} dem - giam {giam_gia*100}%: {tong_tien}")
            
def chuong8_bai9():
   a = int(input("nhap so a: "))
   for i in range(a,0,-1):
    print(i)


def chuong8_bai10():
   n = int(input("Nhap so nguyen n: "))
   x = float(input("Nhap so thuc x: "))
   s = (x**2 + 1)**n
   print(f"S = ({x}^2 + 1)^{n} = {s}")

def chuong8_bai11():
   n = int(input("Nhap so nguyen n: "))
   x = float(input("Nhap so thuc x: "))
   a = (x**2 + x + 1)**n + (x**2 - x + 1)**n
   print(f"A = ({x}^2 + {x} + 1)^{n} + ({x}^2- {x} + 1)^{n} = {a}")

def chuong8_bai12():
 x = int(input("Nhap vao so nguyen duong x: "))
 if x < 2:
     print(f"{x} khong phai so nguyen to")
 else:
    for i in range(2,x):
        if x%i == 0:
            print(f"{x} khong phai so nguyen to")
            break
    else:
        print(f"{x} la so nguyen to")

def chuong8_bai13():
   n = int(input("Nhap vao so nguyen duong n: "))
   tong = 0
   for i in range(0, n+1):
    if i%2!=0:
        tong = tong + i
    print(f"A = {tong}")
    n = int(input("Nhap vao so nguyen duong n: "))
    tich = 1
    for i in range(1, n+1):
     tich = tich*i
    print(f"C = {tich}")
    n = int(input("Nhap vao so nguyen duong n: "))
    tich = 1
    for i in range(1, n+1):
       if i%3==0:
        tich = tich*i
    print(f"D = {tich}")
    n = int(input("Nhap vao so nguyen duong n: "))
    tong = 0
    for i in range(2, n+1):
       for j in range(2,i):
        if i%j == 0:
            break
    else:
        tong = tong + i
    print(f"E = {tong}")
    n = int(input("Nhap vao so nguyen duong n: "))
    tong = 0.0
    flag = True
    for i in range(1, n+1):
      if flag == True:
        tong = tong + 1.0/i
        flag = False
      else:
        tong = tong - 1.0/i
        flag = True
    print(f"F = {tong}")

def chuong8_bai14():
   n = int(input("Nhap so cac so nguyen can tinh: "))
   if n < 0:
    print("n khong hop le")
   else:
    tong = 0
    for i in range(1,n+1):
        k = int(input(f"Nhap so nguyen thu {i}: "))
        tong = tong + k
    print(f"Tong cac so vua nhap: {tong}")

def chuong8_bai15():
   tong = 0
   while True:
      n = int(input("Nhap so nguyen: "))
      print(n)
      tong = tong + n
      if n == 0:
          break
   print(f"Tong cac so vua nhap: {tong}")

def chuong8_bai16():
   a = int(input("Nhap so nguyen a: "))
   b = int(input("Nhap so nguyen b: "))
   if a < 0 or b < 0:
    print("a, b phai lon hon 0")
   min = a
   if min > b:
    min = b
   for i in range(min, 0, -1):
    if a%i == 0 and b%i == 0:
        print(f"UCLN({a},{b}) = {i}")
        break

def chuong8_bai17():
    a = int(input("Nhap so nguyen a: "))
    b = int(input("Nhap so nguyen b: "))
    if a < 0 or b < 0:
        print("a, b phai lon hon 0")
    max = a
    if max < b:
       max = b
    while True:
       if max % a == 0 and max % b == 0:
        print(f"BCNN({a},{b}) = {max}")
        break
    max = max + 1
def chuong8_bai18():
   x = int(input("Nhap vao so nguyen duong x: "))
   if x < 0:
     print("x phai la so nguyen duong")
   else:
      if x == 0:
        print("0 khong phai la so hoan hao")
      tong = 0
      for i in range(1, x):
        if x%i==0:
            tong = tong + i
      if tong == x:
        print(f"{x} la so hoan hao")
      else:
        print(f"{x} khong phai so hoan hao")

def chuong8_bai19():
   day_so = input("Nhap vao mot day so bat ky, moi so cach nhau boi dau cach: ")
#Nhap vao day so "1 3 4 5 6 7 9 10 11 27 13 14 99 16 17 18 21 20"
   if day_so[0] != "1":
    print("Day so phai bat dau tu so 1")
   else:
    day_so_nguoc = day_so[::-1]
    pos = 0
    count = 0
    day_so_moi = ""
    for i in day_so_nguoc:
        if i == " ":
            k = day_so_nguoc[pos - count : pos]
            k = k[::-1]
            if int(k) % 2 != 0:
                day_so_moi = day_so_moi + k + " "
            count = 0
        else:
            count = count + 1
        pos = pos + 1
    day_so_moi = day_so_moi + "1"
    print(day_so_moi)
   

def chuong8_bai20():
   n = int(input("Nhap so nguyen duong n: "))
   x = int(input("Nhap so nguyen x: "))
   if n < 0:
    print("n khong hop le")
   else:
    tong = 0
    for i in range(1,n+1):
        giai_thua = 1
        for j in range(1,i+1):
            giai_thua = giai_thua*i
        tong = tong + (x**i)/giai_thua
    print(f"e^{x} = {tong}")
    
 

