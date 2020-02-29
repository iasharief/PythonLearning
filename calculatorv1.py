operation = str(input("Type 'a' for addition, 's' for subtraction, 'm' for multiplication, 'd' for division, 'sq' for square root, or 'e' for exponents: "))
while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        operation = str(input("Type 'a' for addition, 's' for subtraction, 'm' for multiplication, 'd' for division, 'sq' for square root, or 'e' for exponents: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!5
        #we're ready to exit the loop.
        break
if operation == 'a': 
    addend1 = float(input('First addend:'))
    addend2 = float(input('Second addend:'))
    thesum = addend1 + addend2
    print(addend1 + ' + ' + addend2 + ' = ' + thesum)
else:
    minuend = float(input('Minuend:'))
    subtrahend = float(input('Subtrahend:'))
    thedifference = minuend - subtrahend
    print(minuend + ' - ' + subtrahend + ' = ' + thedifference )