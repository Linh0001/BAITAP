# Kiểm tra số nguyên tố
x=int(input('Nhập số nguyên x = '))
if x<2:
    print("Số",x,"không là số nguyên tố")    
else:
    for i in range(2,x,1):
        if x%i==0:
            print("Số",x,"không phải là số nguyên tố")
            break
    else:
        print("Số",x,"là số nguyên tố")      