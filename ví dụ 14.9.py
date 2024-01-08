try:
    a=int(input("nhập một số nguyên dương nhỏ hơn 100: "))
    #sinh lỗi khi số quá bé
    if a<=0:
        raise ValueError("Bạn đã nhập một số quá nhỏ!")
    if a>=100:
        raise ValueError("bạn cần nhập một số nhỏ hơn 100!")
    #bắt lỗi:
    #nhập số quá lớn
    #nhập số quá bé
except ValueError as ex:
    print(ex)