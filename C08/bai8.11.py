#Nhập vào số nguyên n
print("Nhập n:")
n=int(input())
#Nhập vào số thực x
print("Nhập x:")
x=float(input())
# Tính A
A=(((x*x)+x+1)**n)+(((x*x)-x+1)**n)
print("A=(x*x +x+1)^n + (x*x -x + 1)^n =",A)
