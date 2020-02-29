import time
from random import *
def addition():
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
def subtraction():
	numberofquestions = int(input('How many questions? '))
	right = 0 
	wrong = 0
	lee_number = numberofquestions
	while numberofquestions > 0:
		num1 = randint(500, 1000)
		num2 = randint(1, 500)
		answer = int(input('{} + {} = '.format(num1, num2)))
		numberofquestions -= 1
		if answer == num1 - num2:
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
def multiplication():
	numberofquestions = int(input('How many questions? '))
	right = 0 
	wrong = 0
	lee_number = numberofquestions
	while numberofquestions > 0:
		num1 = randint(500, 1000)
		num2 = randint(1, 500)
		answer = int(input('{} * {} = '.format(num1, num2)))
		numberofquestions -= 1
		if answer == num1 * num2:
		right += 1
		if numberofquestions == 0:
			print ('Correct, goodbye!')
			time.sleep(2)
			print('You got {} out of {} correct. Good work.'.format(right, lee_number))
		else:
			print('Correct!')
		if answer != num1 * num2:
		wrong += 1
		if numberofquestions == 0:
			print ('Sorry, incorrect. Thanks for trying!')
			time.sleep(2)
			print('You got {} out of {} correct. Good work.'.format(right, lee_number))
		else:
			print('Incorrect, I am rooting for you! \nLet\'s get the next one one right, ok?')


def divsion():
	numberofquestions = int(input('How many questions? '))
	right = 0 
	wrong = 0
	lee_number = numberofquestions
	input('PLEASE ONLY ANSWER WITH ONE ROUNDED DECIMAL OR ELSE IT WILL BE MARKED WRONG.')
	while numberofquestions > 0:
		num1 = randint(1, 1000)
		num2 = randint(1, 500)
		answer = int(input('{} / {} = '.format(num1, num2)))
		numberofquestions -= 1
		if answer == round(num1 / num2, 1):
		right += 1
		if numberofquestions == 0:
			print ('Correct, goodbye!')
			time.sleep(2)
			print('You got {} out of {} correct. Good work.'.format(right, lee_number))
		else:
			print('Correct!')
		if answer != round(num1 / num2, 1):
		wrong += 1
		if numberofquestions == 0:
			print ('Sorry, incorrect. Thanks for trying!')
			time.sleep(2)
			print('You got {} out of {} correct. Good work.'.format(right, lee_number))
		else:
			print('Incorrect, I am rooting for you! \nLet\'s get the next one one right, ok?')






operation = str(input('What do you want to be quizzed on? \n Type the number for it: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Floor Division \n 6. Modulus \n 7. Exponents \n 8. Square Root \n 9. Mixed equations \n 10. Word problems \n Please only type the number next to what you want to do: '))
switch(operation) {
	case 1:
		addition()
	case 2: 
		subtraction()
	case 3:
		multiplication()
	case 4:
		divsion()
	default:
		print('Invalid response.')
}
