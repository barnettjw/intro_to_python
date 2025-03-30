#%%
def caps_long(my_string):
    if len(my_string) > 10:
        return my_string.upper()
    else:
        return my_string
# %%
print(caps_long("Sue Smith"))     # Sue Smith
print(caps_long("Sue Roberts"))   # SUE ROBERTS
print(caps_long("Joe Shea"))      # Joe Shea
print(caps_long("Joe Stevens"))   # JOE STEVENS
# %%
