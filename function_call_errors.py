def add_numbers(a, b):      # syntax error
    sum = a + b     # logical error
    return sum

x, y = 10, 11

print(f"The of {x} and {y} is: " + add_numbers(x))   # fstring syntax + concat + function call error
