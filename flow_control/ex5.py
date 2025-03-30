def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

# outputs 'Empty' because empty list literals are falsy,
# so the `else` block runs