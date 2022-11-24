#Giải phương trình bậc nhất ax+b=0
a=eval(input('Nhập a = '))
b=eval(input('Nhập b = '))
if a==0:
    if b==0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm ")
else:
    x=-b/a
    print('Phương trình có nghiệm x =',x)        
0