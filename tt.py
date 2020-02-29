	numberofquestions = int(input('How many questions? '))
	right = 0 
	wrong = 0
	lee_number = numberofquestions
	while numberofquestions > 0:
		num1 = randint(1, 1000)
		num2 = randint(1, 1000)
		answer = int(input('{} + {} = '.format(num1, num2)))
		numberofquestions -= 1
		if answer == num1 + num2:
		right += 1
		if numberofquestions == 0:
			print ('Correct, goodbye!')
			time.sleep(2)
			print('You got {} out of {} correct. Good work.'.format(right, lee_number))
		else:
			print('Correct!')
		if answer != num1 + num2:
		wrong += 1
		if numberofquestions == 0:
			print ('Sorry, incorrect. Thanks for trying!')
			time.sleep(2)
			print('You got {} out of {} correct. Good work.'.format(right, lee_number))
		else:
			print('Incorrect, I am rooting for you! \nLet\'s get the next one one right, ok?')
