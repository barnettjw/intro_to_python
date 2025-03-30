def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# say   --> function name
# print --> built-in function name
# input --> built-in function name
# max   --> built-in function name
# upper --> method name
# lower --> method name