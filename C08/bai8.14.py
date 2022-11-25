# Tính tổng của N số nguyên nhập vào
print("Chương trình tính tổng N số nguyên:")
n=int(input("N = "))
mylist=[]
for i in range(n):
    val=int(input("Nhập số nguyên : "))
    mylist.append(val)
S=0
for i in mylist:
    S+=i
print("S =",S)    


