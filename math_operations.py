def addition(numbers):
    total = sum(numbers)
    print('The total is', total)

def subtraction(numbers):
    for x in numbers:
        x = (-1)*x
    total = sum(numbers)
    print('The total is', total)