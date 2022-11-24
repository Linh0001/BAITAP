#Tính tiền điện
print("Nhập số Kwh ")
so_Kwh=int(input('so_Kwh ='))
if so_Kwh <0:
    print("Vui lòng nhập số kwh lớn hơn 0")
elif so_Kwh<=50:
    Tien_dien=so_Kwh*1678
elif so_Kwh<=100:
    Tien_dien=(50*1678)+((so_Kwh-50)*1734)
elif so_Kwh<=200:
    Tien_dien=(50*1678)+(50*1734)+((so_Kwh-100)*2014)
elif so_Kwh<=300:
    Tien_dien=(50*1678)+(50*1734)+(100*2014)+((so_Kwh-200)*2563)
elif so_Kwh<=400:
    Tien_dien=(50*1678)+(50*1734)+(100*2014)+(100*2563)+((so_Kwh-300)*2834)
else :
    Tien_dien=(50*1678)+(50*1734)+(100*2014)+(100*2563)+(100*2834)+((so_Kwh-400)*2927)            
print("Tiền điện phải trả là :",Tien_dien,"vnđ") 


