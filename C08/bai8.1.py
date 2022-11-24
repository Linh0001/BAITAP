# Viết chương trình tìm số lớn nhất -số nhỏ nhất
a=int(input('a= '))
b=int(input('b= '))
c=int(input("c= "))
d=int(input('d= '))
S=[a,b,c,d]
max=a
min=a
for i in S:
    if max < i:
            max = i
    elif min > i:
            min = i
print('Max =',max)
print("Min =",min)

    
       
