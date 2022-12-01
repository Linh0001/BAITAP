#Tính BMI và in ra đánh giá
import math
def tinh_bmi(cn,cc):
    bmi=cn/math.pow(cc,2)
    return bmi
def danh_gia(bmi):
	if bmi<18.5:
		return 'Bạn đang ở trạng thái gầy'
	elif 18.5<=bmi<=24.99:
		return 'Bạn đang ở trạng thái bình thường'
	else:
		return'Bạn đang ở trạng thái thừa cân'		
cn=int(input("Nhập cân nặng (kg): "))
cc=float(input("Nhập chiều cao (m): "))    
bmi=tinh_bmi(cn,cc)
print("BMI = %0.2f"%bmi)
print(danh_gia(bmi))

	
