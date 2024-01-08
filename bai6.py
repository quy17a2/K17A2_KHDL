num = int(input("Nhập số nguyên: "))
sum = 0
num_str = str(num)
for digit in num_str:
    sum += int(digit)

print("Tổng các chữ số của", num, "là:", sum)