#Tính cước taxi
Loai_xe=int(input('Vui lòng chọn loại xe 4 hay 7 chỗ :'))
So_km=float(input('Số km đã chạy :'))
Thoi_gian_cho=float(input('Thời gian chờ (phút) :'))
if Thoi_gian_cho>5:
    Tien_cho=(Thoi_gian_cho-5)*800
else:
    Tien_cho=0
# Xe 4 chỗ    
if Loai_xe==4:
    if So_km <=0.8:
        Tien_cuoc=11000+Tien_cho
    elif So_km<=20:
        Tien_cuoc=11000+((So_km-0.8)*12000)+Tien_cho
    else:
        Tien_cuoc=11000+((20-0.8)*12000)+((So_km-20)*10000)+Tien_cho 
    print("Tiền cước taxi phải trả là :",Tien_cuoc)
# Xe 7 chỗ  
if Loai_xe==7:
    if So_km <=0.8:
        Tien_cuoc=13000+Tien_cho
    elif So_km<=30:
        Tien_cuoc=13000+((So_km-0.8)*14100)+Tien_cho
    else:
        Tien_cuoc=13000+((30-0.8)*14100)+((So_km-30)*12000)+Tien_cho 
    print("Tiền cước taxi phải trả là :",Tien_cuoc)          


