#Tính diện tích tam giác biết số đo 3 cạnh a,b,c theo công thức Hero
import math   #import thư viện toán học để sử dụng hàm tính căn bậc 2 , sqrt
print("Nhập số đo 3 cạnh của tam giác ABC:")
a=eval(input('Số đo cạnh a = '))
b=eval(input('Số đo canh b = '))
c=eval(input('Số đo cạnh c = '))
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác ABC đã cho là :",s)