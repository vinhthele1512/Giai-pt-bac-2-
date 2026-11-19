#Le_The_Vinh
#Giai pt bac 2___Solve quadratic equations 
#Input of a,b,c
while True:
	while True:
		try:
			a=float(input("Enter number a: "))
			break
		except ValueError:
			print("You are not allowed to enter any characters other than numbers.")
	while True:
			try:
				b=float(input("Enter number b: "))
				break
			except ValueError:
				print("You are not allowed to enter any characters other than numbers.")
	while True:
			try:
				c=float(input("Enter number c: "))
				break
			except ValueError:
				print("You are not allowed to enter any characters other than numbers.")
#Caculate delta
	d=b**2-4*a*c
#Set conditions
	if a==0 and b==0 and c==0:
			print("The equation has infinitely many solutions.")
	elif a==0 and b==0:
			print("The equation has no solution.")
	elif a==0 and c==0:
		ans=c/b
		print("The equation has one solution.")
		print("x=",ans)
	elif b==0 and c==0:
		print("The equation has one solution.")
		print("x= 0")
	elif a==0:
			ans0=-c/b
			print("The equation has one solution.")
			print("x=",ans0)
	elif d>0:
			ans1=(-b+d**0.5)/(2*a)
			ans2=(-b-d**0.5)/(2*a)
			print("The equation has two distinct solutions.")
			print("x1=",ans1)
			print("x2=",ans2)
	elif d==0:
			ans3=(-b)/(2*a)
			print("The equation has a double root.")
			print("x1= x2=",ans3)
	else:
			print("The equation has no solution.")
	again=input("Select 1 to stop, select any to continue: ")
	if again=="1":
		break
#End
#Thanks for watching my files!
#Ltvih
#2012
		