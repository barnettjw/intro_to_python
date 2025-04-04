#%%
my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

#%%
def find_integers(my_tuple):
    return [val for val in my_tuple
            if (type(val) is int)]

integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]

# %%
