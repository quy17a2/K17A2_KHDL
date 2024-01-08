alice_candies=121
bob_candies=77
carol_candies=109
to_smash=(alice_candies+bob_candies+carol_candies)%3
print("số kẹo phải đập là =",to_smash)
#1.7
Nhiet_do = float(input("Nhập nhiệt độ: "))
Do_F = ((Nhiet_do) * 9/5) + 32
print(f"{Nhiet_do:.2f} độ C = {Do_F:.2f} độ F")
#1.8
s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")
s3 = input("Nhập chuỗi s3: ")
index = int(input("Nhập chỉ mục index: "))
chieu_dai_s1 = len(s1)
chieu_dai_s2 = len(s2)
chieu_dai_s3 = len(s3)
print(f"Chiều dài của chuỗi s1: {chieu_dai_s1}")
print(f"Chiều dài của chuỗi s2: {chieu_dai_s2}")
print(f"Chiều dài của chuỗi s3: {chieu_dai_s3}")
s4 = s1[index:]
lap_lai_chuoi_s2 = s2 * 2
print(f"Chuỗi con s4 từ index đến hết: {s4}")
print(f"Chuỗi s2 lặp lại 2 lần: {lap_lai_chuoi_s2}")
#1.9
lai_suat_nam = float(input("Lãi suất 1 năm (%): "))
so_tien_gui = float(input("Số tiền gửi (VNĐ): "))
so_thang_gui = int(input("Số tháng gửi: "))
lai_suat_thang = lai_suat_nam/100/12
tien_lai = (so_tien_gui * so_thang_gui) * lai_suat_thang
tong_so_tien = so_tien_gui + tien_lai
print(f"Tiền lãi = {tien_lai:.1f} ")
print(f"Tiền vốn + lãi = {so_tien_gui:.0f} + {tien_lai:.0f} = {tong_so_tien:.0f}")
