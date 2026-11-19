#Le_The_Vinh
#Giai pt bac 2___Solve quadratic equations 
#Dau vao cua a,b,c
while True:
	while True:
		try:
			a=float(input("Nhap so a: "))
			break
		except ValueError:
			print("Ban khong duoc nhap ki tu ngoai so!")
	while True:
			try:
				b=float(input("Nhap so b: "))
				break
			except ValueError:
				print("Ban khong duoc nhap ki tu ngoai so!")
	while True:
			try:
				c=float(input("Nhap so c: "))
				break
			except ValueError:
				print("Ban khong duoc nhap ki tu ngoai so!")
#Tinh delta
	d=b**2-4*a*c
#Dat dieu kien
	if a==0 and b==0 and c==0:
			print("Pt co vo so nghiem!")
	elif a==0 and b==0:
			print("Pt vo nghiem!")
	elif a==0:
			e0=-c/b
			print("Pt co 1 nghiem!")
			print("x=",e0)
	elif d>0:
			nghiem1=(-b+d**0.5)/(2*a)
			nghiem2=(-b-d**0.5)/(2*a)
			print("Pt co 2 nghiem pb!")
			print("x1=",nghiem1)
			print("x2=",nghiem2)
	elif d==0:
			e1=(-b)/(2*a)
			print("Pt co nghiem kep!")
			print("x1= x2=",e1)
	elif d<0:
			print("Pt vo nghiem!")
	try:
			again=input(" Chon 1 de dung lai, chon bat ki de dung tiep: ")
			if again=="1":
				break
			else:
				continue
	except:
		print("")
#End
#Thanks for watching my files!
#Ltvih
#2012
			
			