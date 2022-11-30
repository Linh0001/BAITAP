print("Nhập dãy số bắt đầu bằng số 1 : ")
n=int(input("Nhập số lượng số trong dãy số: "))
i=int(1)
day_so=""
while i<n:
    i=int(input("i= "))
    day_so += str(i)
print("Đảo ngược dãy số và in ra các số lẻ: ")
kq=""
for ch in day_so:
    kq=ch+kq
for ch in kq:
    if int(ch)%2 !=0:
        print(ch,end=" ")    





  
      