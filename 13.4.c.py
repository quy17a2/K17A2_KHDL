f =open("bai_tho.txt",'r',encoding='utf-8')
a =f.readline()
print('Nội dung dòng đầu: ',(a))
b=f.readlines()
print('Nội dung các dòng còn lại:\n',(b))
c=f.readlines()
print('Nội dung các dòng còn lại:\n',(c))
f.close