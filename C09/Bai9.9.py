# Sử dụng biểu thức lamda để tính diện tích,chu vi hình tròn tham số r (bán kính)
import math
def hinh_tron(r):
    sht =math.pi*math.pow(r,2)
    pht =2*math.pi*r
    return sht,pht
def hinh_chu_nhat(a,b):
    scn=a*b
    pcn=2*(a+b)
    return scn,pcn
r=float(input("Bán kính r = "))
a=float(input("Chiều dài hình chữ nhật a = "))
b=float(input("Chiều rộng hình chữ nhật b = "))
sht,pht=hinh_tron(r)
scn,pcn=hinh_chu_nhat(a,b)
print("S hình tròn = %0.2f"%sht)
print("P hình tròn = %0.2f"%pht)
print("S hình chữ nhật = %0.2f"%scn)
print("P hình chữ nhật = %0.2f"%pcn)

