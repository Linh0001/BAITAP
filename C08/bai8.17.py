#Tính BCNN(a,b)a,b nhập từ bàn phím
a=int(input('a = '))
b=int(input('b = '))
# Tìm UCLN
for i in range(min(a,b),0,-1):
    if a%i==0 and b%i==0:
        x=int((a*b)/i)   #BCNN(a,b)=(a*b)/UCLN(a,b)
        print("BCNN(a,b) =",x)
    

     
