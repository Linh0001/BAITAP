# Tính diện tích tam giác bằng công thức Heron
print("Nhập số đo 3 cạnh của tam giác ABC:")
a=eval(input('Số đo cạnh a = '))
b=eval(input('Số đo canh b = '))
c=eval(input('Số đo cạnh c = '))
import math
if abs(b-c)<a and a<(b+c):
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Diện tích tam giác ABC đã cho là :",s)
else:
    print("Số đo a,b,c không thoả mãn là 3 cạnh của tam giác")    
