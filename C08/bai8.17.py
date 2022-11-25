#Tính BCNN(a,b)a,b nhập từ bàn phím
a=int(input('a = '))
b=int(input('b = '))
# Cho 1 biến chạy từ giá trị nhỏ nhất của 1 số ngược về 1 nếu 
# cả 2 số đều chia hết cho biến đó thì là ucln 
for i in range(min(a,b),0,-1):
    if a%i==0 and b%i==0:
        x=int((a*b)/i)
        print("BCNN(a,b) =",x)
    

     