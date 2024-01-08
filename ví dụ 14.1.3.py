def tinhTB(hk1,hk2):
    assert(hk1 >=0 and hk2 >=0) ,'cả điểm hk1 và hk2 phải >=0!'
    tb=(hk1+hk2*2)/3
    return tb
print(tinhTB(8,7.5))

print(tinhTB(-1,6))