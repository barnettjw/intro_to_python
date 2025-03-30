foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# prints `bar` because of where print() is called
# in the global scope, the value of `foo` is `bar`
