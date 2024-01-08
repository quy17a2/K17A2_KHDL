N = int(input("Nhập số tự nhiên N: "))
for i in range(1, N+1):
    print(i)

num = int(input("Nhập số nguyên: "))
sum = 0
num_str = str(num)
for digit in num_str:
    sum += int(digit)

print("Tổng các chữ số của", num, "là:", sum)