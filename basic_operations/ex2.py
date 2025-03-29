# %%
number = 4936
thousands = number // 1000
remaining = number - (thousands * 1000)
hundreds = remaining // 100
remaining = remaining - (hundreds * 100)
tens = remaining // 10
remaining = remaining - (tens * 10)
ones = remaining

print(ones)
print(tens)
print(hundreds)
print(thousands)
