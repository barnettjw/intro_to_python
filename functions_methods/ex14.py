def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# line 1:   multiply, left, right
# line 2:   left, right
# line 3:
# line 4:   get_num, prompt
# line 5:   input, prompt
# line 6:
# line 7:   first_number, get_num
# line 8:   second_number, get_num
# line 9:   product, multiply, first_number, second_number
# line 10:  print, first_number, second_number, product