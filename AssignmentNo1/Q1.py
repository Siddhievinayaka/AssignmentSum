# Perform Basic Mathematical Operations
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


# Using the functions


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))


print(f"\n\nAddition: {x} + {y} = {add(x, y)}")
print(f"Subtraction: {x} - {y} = {subtract(x, y)}")
print(f"Multiplication: {x} * {y} = {multiply(x, y)}")
print(f"Division: {x} / {y} = {divide(x, y)}")
