while True:
	try:
		starting_which_one = str(input("Type 'c' for Celsius or 'f' for Fahrenheit:"))
	except ValueError:
		print("Let's try again")
		continue
	else:
		break
if starting_which_one == 'f':
	far = float(input('Fahrenheit number: ' ))
	cel = 5 / 9 * (far - 32)
	print('The number in celsius is {:.2f}.'.format(cel))
else: 
	far2 = float(input('Celsius number:'))
	cel2 = (far2 * 1.8) + 32
	print('El número en grados Fahrenheit es : {:.2f}.'.format(cel2))