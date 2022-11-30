import math
x=int(input("Nhập x = "))
Ex=1
n=1
t=x
while math.fabs(t)>=0.0001:
     Ex+=t
     n+=1
     t=t*(x/(float(n)))
print("Giá trị gần đúng của e mũ x là : %0.6f"%Ex)     




     

   