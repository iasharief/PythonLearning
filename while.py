#Hello! This is a calculator project that can be used for sqrt, exponents, addition, subtraction, multiplication, and division. Try it out! 
while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        operation = str(input("Type 'a' for addition, 's' for subtraction, 'm' for multiplication, 'd' for division, 'sq' for square root, or 'e' for exponents: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break
if operation == 'a': 
    addend1 = float(input('First addend:'))
    addend2 = float(input('Second addend:'))
    thesum = addend1 + addend2
    print(addend1, ' + ', addend2, ' = ', thesum)
    print('¡Chau!')
if operation == 's':
    minuend = float(input('Minuend:'))
    subtrahend = float(input('Subtrahend:'))
    thedifference = float(minuend - subtrahend)
    print(minuend, ' - ', subtrahend, ' = ', thedifference )
    print('¡Chau!')
if operation == 'm':
    factor1 = float(input('First factor:'))
    factor2 = float(input('Second factor:'))
    theproduct = float(factor1 * factor2)
    print(factor1, ' * ', factor2, ' = ', theproduct)
    print('¡Chau!')
if operation == 'd':
    dividend = float(input('Dividend:'))
    divisor = float(input('Divisor:'))
    thequotient = float(dividend / divisor)
    print(dividend, ' / ', divisor, ' = ', thequotient )
    print('¡Chau!')
if operation == 'sq': 
    sqrtnumber = float(input('Square Root Starting number:'))
    sqrtanswer = sqrtnumber ** 0.5
    print('The square root of ', sqrtnumber, ' is ', sqrtanswer, '.')
    print('¡Chau!')
if operation == 'e':
    bigex = float(input('Big number:'))
    smallex = float(input('Small number:'))
    answerex = float(bigex ** smallex)
    print(bigex, ' to the power of ', smallex, ' equals ', answerex, '.')
    print('¡Chau!')