# Tính tiền thuê phòng của resort
a = int(input(" Cho biết loại phòng:"))
b = int(input(" cho biết số đêm ở: "))
# Loại phòng 1 
if a == 1:
    n= 1260
elif a==2:
    n=1550
elif a==3 and a==4:
    n=1830
elif a==5 and a==6:
    n=2120
elif a==7:
    n=2540
elif a==8:
    n=4800
if a and b == 1:
    t = n*b
elif  1<b<=3: 
    t = (a*b)*75/100
else: 
    t = (a*b)*70/100
    print("Số tiền phải trả là:", t, "đồng")
   
   
    
