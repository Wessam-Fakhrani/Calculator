import math_operations as maths
import time

def sanitization(value, acceptables) -> bool:
    if value in acceptables:
        return True
    else:
        return False

reset = True

while reset == True:
    print('Welcome to the Calculator.')
    print('A) Addition \nB) Subtraction \nC) Multiplication \nD) Division \n\n')
    time.sleep(1)

    while True:
        operation = input('Please select one of the above: ')
        operation = operation.upper()
        if sanitization(operation, ['A', 'B', 'C', 'D']) == False:
            print("Input Invalid, Try again! \n")
        else:
            print("Input accepted. \n")
            break
    
    if operation == 'A':
        x = input("Please enter the values you would like to add together, separated by spaces\n")
        values = x.split(' ')
        values2 = [eval(x) for x in values]
        maths.addition(values2)
    
    elif operation == 'B':
        x = input("Please enter the values you would like to subtract, separated by spaces. The first value will be the value all the others will be subtracted from\n")
        values = x.split(' ')
        values2 = [eval(x) for x in values]
        maths.subtraction(values2)

    elif operation == 'C':
        x = input("Please enter the values you would like to multiply, separated by spaces\n")
        values = x.split(' ')
        values2 = [eval(x) for x in values]
        maths.multiplication(values2)
    