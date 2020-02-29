import time
user_input = str(input('Enter 5 numbers separated with spaces '))
numberlist = user_input.split()
value1 = numberlist[0]
try:
	val1 = int(value1)
	#print("Input is valid. ")
	i=5
	while (i > 0 and i < 6):
		print(i, '...')
		time.sleep(1)
		i -= 1
	remainder1 = val1 % 2
	if remainder1 == 0:
		print('Yay! {} is an even number!'.format(val1))
	elif remainder1 == 1:
		print('Yay! {} is an odd number!'.format(val1))
	else:
		print('none')
except ValueError:
	try:
		val1 = float(value1)
		print("Input is a float number. Number = ", val1)
	except ValueError:
		print("No.. input is not a number. It's a string")

value2 = numberlist[1]
try:
	val2 = int(value2)
	#print("Input is valid. ")
	i=5
	while (i > 0 and i < 6):
		print(i, '...')
		time.sleep(1)
		i -= 1
	remainder2 = val2 % 2
	if remainder2 == 0:
		print('Yay! {} is an even number!'.format(val2))
	elif remainder2 == 1:
		print('Yay! {} is an odd number!'.format(val2))
	else:
		print('none')
except ValueError:
	try:
		val2 = float(value2)
		print("Input is a float number. Number = ", val2)
	except ValueError:
		print("No... input is not a number. It's a string")
value3 = numberlist[2]
try:
	val3 = int(value3)
	#print("Input is valid. ")
	i=5
	while (i > 0 and i < 6):
		print(i, '...')
		time.sleep(1)
		i -= 1
	remainder3 = val3 % 2
	if remainder3 == 0:
		print('Yay! {} is an even number!'.format(val3))
	elif remainder3 == 1:
		print('Yay! {} is an odd number!'.format(val3))
	else:
		print('none')
except ValueError:
	try:
		val3 = float(value3)
		print("Input is a float number. Number = ", val3)
	except ValueError:
		print("No.. input is not a number. It's a string")
value4 = numberlist[3]
try:
	val4 = int(value4)
	#print("Input is valid. ")
	i=5
	while (i > 0 and i < 6):
		print(i, '...')
		time.sleep(1)
		i -= 1
	remainder4 = val4 % 2
	if remainder4 == 0:
		print('Yay! {} is an even number!'.format(val4))
	elif remainder1 == 1:
		print('Yay! {} is an odd number!'.format(val4))
	else:
		print('none')
except ValueError:
	try:
		val4 = float(value4)
		print("Input is a float number. Number = ", val4)
	except ValueError:
		print("No.. input is not a number. It's a string")
value5 = numberlist[4]
try:
	val5 = int(value5)
	#print("Input is valid. ")
	i=5
	while (i > 0 and i < 6):
		print(i, '...')
		time.sleep(1)
		i -= 1
	remainder5 = val5 % 2
	if remainder5 == 0:
		print('Yay! {} is an even number!'.format(val5))
	elif remainder5 == 1:
		print('Yay! {} is an odd number!'.format(val5))
	else:
		print('none')
except ValueError:
	try:
		val5 = float(value5)
		print("Input is a float number. Number = ", val5)
	except ValueError:
		print("No.. input is not a number. It's a string")