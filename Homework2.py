import random
def input_function():
    try:
        global  min
        min = int(input("Enter a range of integers from 1 to 1000, starting with min (from 1 to 999): "))
        if min > 999 or min < 1:
            print("Input error, try again")
            input_function()
        global max
        max = int(input(f"Max from {min} to 1000: "))
        if max <= min or 1000 < max:
            print('Input error, the max value must be greater than min and up to 1000 incusive, try again!')
            input_function()
        global quantity
        quantity = int(input(f"Enter the quantity of numbers from 1 to {max - min + 1}: "))
        if quantity < 1 or (max - min + 1) < quantity:
             print('Input error,be more careful! Try again!')
             input_function()
    except ValueError:
        print("Input error, enter integers according to the conditions!")
        input_function()
    return [min, max, quantity]
a = input_function()
min= a[0]
max= a[1]
quantity = a[2]

def get_numbers_ticket (min,max,quantity):
    tickets_set = set()
    while len(tickets_set) < quantity:
        ticket = random.randint(min, max)
        tickets_set.add(ticket)
    lottery_numbers = list(tickets_set)
    lottery_numbers.sort()
    return lottery_numbers
print(f'Congratulations! Your lottery numbers: {get_numbers_ticket(min, max, quantity)}')import random
def input_function():
    try:
        global  min
        min = int(input("Enter a range of integers from 1 to 1000, starting with min (from 1 to 999): "))
        if min > 999 or min < 1:
            print("Input error, try again")
            input_function()
        global max
        max = int(input(f"Max from {min} to 1000: "))
        if max <= min or 1000 < max:
            print('Input error, the max value must be greater than min and up to 1000 incusive, try again!')
            input_function()
        global quantity
        quantity = int(input(f"Enter the quantity of numbers from 1 to {max - min + 1}: "))
        if quantity < 1 or (max - min + 1) < quantity:
             print('Input error,be more careful! Try again!')
             input_function()
    except ValueError:
        print("Input error, enter integers according to the conditions!")
        input_function()
    return [min, max, quantity]
a = input_function()
min= a[0]
max= a[1]
quantity = a[2]

def get_numbers_ticket (min,max,quantity):
    tickets_set = set()
    while len(tickets_set) < quantity:
        ticket = random.randint(min, max)
        tickets_set.add(ticket)
    lottery_numbers = list(tickets_set)
    lottery_numbers.sort()
    return lottery_numbers
print(f'Congratulations! Your lottery numbers: {get_numbers_ticket(min, max, quantity)}')
