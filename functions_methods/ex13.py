def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# This will raise an error, a positional parameter is defined after a parameter with a default