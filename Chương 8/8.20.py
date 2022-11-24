# Tính tiền thuê phòng của resort
a = int(input(" Cho biết loại phòng:"))
b = int(input(" cho biết số đêm ở: "))
# Loại phòng 1 
if a == 1 and b == 1:
    t= (1260000*b)
elif a==1 and 1<b<=3:
    t=(1260000*b)*75/100
else:
    t=(1260000*b)*70/100
# Loại phòng 2
if  a==2 and b == 1:
    t = 1550000*b
elif a==2 and 1<b<=3: 
    t = (1550000*b)*75/100
else: 
    t = (1550000*b)*70/100  
# Loại phòng 3, 4
if a==3 and a==4 and b==1:
    t=(1830000*b)
elif a==3 and a==4 and 1<b<=3:
    t=(1830000*b)*75/100
else:
    t=(1830000*b)*70/100   
# Loại phòng 5,6
if a==5 and a==6 and b == 1:
    t = 2120000*b
elif  a==5 and a==6 and 1<b<=3: 
    t = (2120000*b)*75/100
else: 
    t = (2120000*b)*70/100 
#Loại phòng 7
if a==7 and b == 1:
    t = 2540000*b
elif a==7 and 1<b<=3: 
    t = (2540000*b)*75/100
else: 
    t = (2540000*b)*70/100
# Loại phòng 8 
if a==8 and b == 1:
    t = 4800000*b
elif  a==8 and 1<b<=3: 
    t = (4800000*b)*75/100
else: 
    t = (4800000*b)*70/100
    print("Số tiền phải trả là: ", t, "đồng")
   
    
    