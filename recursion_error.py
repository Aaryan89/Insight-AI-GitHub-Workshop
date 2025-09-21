def factorial(n):
    return n * factorial(n-1)

a, b, c = 5, 0, -4
print(f"Factorial of {a}", factorial(a))
print(f"Factorial of {a}", factorial(b))
print(f"Factorial of {c}", factorial(c))