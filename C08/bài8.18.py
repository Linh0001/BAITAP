# Kiểm tra số hoàn hảo
# Số hoàn hảo là số có tổng các ước nguyên dương bằng chính nó
n=int(input("Nhập số cần kiểm tra :"))
tong=0
for i in range(1,n,1):
    if n%i==0:
        tong +=i
if tong==n:
    print("Số",n,"là số hoàn hảo") 
else:
    print("Số",n,"không là số hoàn hảo")
