#!/usr/bin/env python3
import time
from random import *
def addition(x):
	right = 0 
	wrong = 0
	lee_number = x
	while x > 0:
		num1 = randint(1, 1000)
		num2 = randint(1, 1000)
		answer = int(input('{} + {} = '.format(num1, num2)))
		x -= 1
		if answer == num1 + num2:
			right += 1
			if x == 0:
				print('Correct, goodbye!')
				time.sleep(2)
				print('You got {} out of {} correct. Good work.'.format(right, lee_number))
			else:
				print('Correct!')
		if answer != num1 + num2:
			wrong += 1
			if x == 0:
				print('Sorry, incorrect. Thanks for trying!')
				time.sleep(2)
				print('You got {} out of {} correct. Good work.'.format(right, lee_number))
			else:
				print('Incorrect, I am rooting for you! \nLet\'s get the next one one right, ok?')
def subtraction(x):
	right = 0 
	wrong = 0
	lee_number = x
	while x > 0:
		num1 = randint(500, 1000)
		num2 = randint(1, 500)
		answer = int(input('{} - {} = '.format(num1, num2)))
		x -= 1
		if answer == num1 - num2:
			right += 1
			if x == 0:
				print ('Correct, goodbye!')
				time.sleep(2)
				print('You got {} out of {} correct. Good work.'.format(right, lee_number))
			else:
				print('Correct!')

		if answer != num1 - num2:
			wrong += 1
			if x == 0:
				print ('Sorry, incorrect. Thanks for trying!')
				time.sleep(2)
				print('You got {} out of {} correct. Good work.'.format(right, lee_number))
			else:
				print('Incorrect, I am rooting for you! \nLet\'s get the next one one right, ok?')
def multiplication(x):
	right = 0 
	wrong = 0
	lee_number = x
	while x > 0:
		num1 = randint(500, 1000)
		num2 = randint(1, 500)
		answer = int(input('{} * {} = '.format(num1, num2)))
		x -= 1
		if answer == num1 * num2:
			right += 1
			if x == 0:
				print ('Correct, goodbye!')
				time.sleep(2)
				print('You got {} out of {} correct. Good work.'.format(right, lee_number))
			else:
				print('Correct!')
		if answer != num1 * num2:
			wrong += 1
			if x == 0:
				print ('Sorry, incorrect. Thanks for trying!')
				time.sleep(2)
				print('You got {} out of {} correct. Good work.'.format(right, lee_number))
			else:
				print('Incorrect, I am rooting for you! \nLet\'s get the next one one right, ok?')


def divsion(x):
	right = 0 
	wrong = 0
	lee_number = x
	input('PLEASE ONLY ANSWER WITH ONE ROUNDED DECIMAL OR ELSE IT WILL BE MARKED WRONG.')
	while x > 0:
		num1 = randint(12, 1000)
		num2 = randint(1, 12)
		answer = float(input('{} / {} = '.format(num1, num2)))
		x -= 1
		if answer == round(num1 / num2, 1):
			right += 1
			if x == 0:
				print ('Correct, goodbye!')
				time.sleep(2)
				print('You got {} out of {} correct. Good work.'.format(right, lee_number))
			else:
				print('Correct!')
		if answer != round(num1 / num2, 1):
			wrong += 1
			if x == 0:
				print ('Sorry, incorrect. Thanks for trying!')
				time.sleep(2)
				print('You got {} out of {} correct. Good work.'.format(right, lee_number))
			else:
				print('Incorrect, I am rooting for you! \nLet\'s get the next one one right, ok?')






operation = int(input('What do you want to be quizzed on? \n Type the number for it: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Floor Division \n 6. Modulus \n 7. Exponents \n 8. Square Root \n 9. Mixed equations \n 10. Word problems \n Please only type the number next to what you want to do: '))
num_of_questions = int(input('How many questions do you want?'))
if operation == 1:
	addition(num_of_questions)
if operation == 2:
	subtraction(num_of_questions)
if operation == 3:
	multiplication(num_of_questions)
if operation == 4:
	divsion(num_of_questions)
