# Tính tổng của các số nguyên nhập vào, chấm dứt khi nhập số 0
print("Chương trình tính tổng N số nguyên:")
mylist=[]
while True:
    val=int(input("Nhập một số nguyên (kết thúc bằng số 0) :"))
    if val==0:
        mylist=[val]
        S=0
    for i in mylist:
        S=S+i
        print("S =",S)  
        break         


        
   
