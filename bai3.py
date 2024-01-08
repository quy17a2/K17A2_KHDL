m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))

for i in range(1, n+1):
    if i % m == 0:
        print(i)
