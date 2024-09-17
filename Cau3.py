try:
	toan=float(input("Nhap diem toan: "))
	ly=float(input("Nhap diem ly: "))
	hoa=float(input("Nhap diem hoa: "))
	dtb=(toan+ly+hoa)/3
	print("Ket qua: ",round(dtb,2))
except ValueError:
	print("Error")