a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

# Tìm ước chung lớn nhất của hai số
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# Tính bội chung nhỏ nhất của hai số
def lcm(x, y):
    return (x * y) // gcd(x, y)

print("Bội chung nhỏ nhất của", a, "và", b, "là:", lcm(a, b))

#bài6

num = int(input("Nhập số nguyên: "))
sum = 0
num_str = str(num)
for digit in num_str:
    sum += int(digit)

print("Tổng các chữ số của", num, "là:", sum)