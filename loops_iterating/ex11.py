#%%
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

#%%
i_out = 0
while i_out < len(my_list):
    i_in = 0
    sub_list = my_list[i_out]
    while i_in < len(sub_list):
        current = sub_list[i_in]
        if current % 2 == 0: print(current)
        i_in += 1
    i_out += 1
# %%
