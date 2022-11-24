# Viết chương trình kiểm tra có phải năm nhuận hay không
x=int(input('Nhập năm cần kiểm tra :'))
if x%4==0 and x%100!=0:
    print("Năm",x,"là năm nhuận")
elif x%400==0:
    print('Năm',x,"là năm nhuận")
else:
    print("Năm",x,"không phải là năm nhuận")
        