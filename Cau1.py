import math

try:	
	r=float(input("Nhap ban kinh: "))
	cv=2*math.pi*r
	dt=math.pi*r*r
	print("Chu vi: ",round(cv,2))
	print("Dien tich: ",round(dt,2))
except ValueError:
	print("error")