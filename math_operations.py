def addition(numbers):
    total = sum(numbers)
    print('The total is', total)

def subtraction(numbers):
    for x in range(1, len(numbers)):
        numbers[x] = numbers[x] * (-1)
    total = sum(numbers)
    print('The total is', total)

def multiplication(numbers):
    total = 1
    for x in range(len(numbers)):
        total = total * numbers[x]
    print('The total is', total)