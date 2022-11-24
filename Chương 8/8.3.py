# Giải phương trình bặc nhất 1 ẩn 
print(" Gải phương trình ax+b=0")
a = int(input("Nhập số a:"))
b = int(input("Nhập số b:"))
if a == 0: 
    if b == 0:
        print("Phương trình vô số nghiệm ")
    else: print("Phương trình vô nghiệm")
else:
    print('Nghiện của phương trình là: x =',-b/a)