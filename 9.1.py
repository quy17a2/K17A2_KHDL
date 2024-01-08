def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

# Kiểm tra phương thức sign
number = float(input("Nhập một số: "))
result = sign(number)

if result == 1:
    print(f"{number} là số 1")
elif result == -1:
    print(f"{number} là số -1.")
else:
    print("là số 0.")

