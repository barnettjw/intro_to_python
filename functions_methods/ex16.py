def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# multiply on lines 1, 9
# left, right on line 1
# get_num on lines 4, 7, 8
# prompt on line 4
# float on line 5
# print on line 10