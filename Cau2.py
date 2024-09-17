try:
	t=int(input("Nhap so giay: "))
	hour=(t//3600)%24
	minute=(t%3600)//60
	second=(t%3600)%60
	period="AM" if hour < 12 else "PM"
	if hour == 0:
		hour == 12
	print(f"{hour}:{minute}:{second} {period}")
except ValueError:
	print("Phát hiện nghi vấn hack 31_0")