def set_foo():
    foo = 'bar'

set_foo()
print(foo) # throws a NameError

# The variable `foo` is scoped in the function set_foo()
# The print is called from the global scope