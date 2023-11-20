import math_operations as maths
import time

def sanitization(value, acceptables) -> bool:
    if value in acceptables:
        return True
    else:
        return False

reset = True

while reset == True:
    operation = 'e'

    print('Welcome to the Calculator.')
    print('A) Addition \nB) Subtraction \nC) Multiplication \nD) Division \n\n')
    time.sleep(1)

    while sanitization(operation.upper(), ['A', 'B', 'C', 'D']) == False:
        operation = input('Please enter a valid letter for the operation: ')

    if operation.upper() == 'A':
        values = input("Please enter all values you would like to add separated by a space\n").split()
        print(values)
