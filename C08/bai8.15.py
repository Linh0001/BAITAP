# Tính tổng của các số nguyên nhập vào, chấm dứt khi nhập số 0
S=0
while True:
     i=eval(input("Nhập một số nguyên (kết thúc là số 0): "))
     S=S+i
     if (i==0):
         print("S =",S)
         break


        
   
