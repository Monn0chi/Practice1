# basic calculator with functions

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

option = input("Choose operation (+, -, *, /): ")
if option == '+':
    print(f"{x} + {y} = {add(x, y)}")
elif option == '-':
    print(f"{x} - {y} = {subtract(x, y)}")
elif option == '*':     
    print(f"{x} * {y} = {multiply(x, y)}")
elif option == '/':
    print(f"{x} / {y} = {divide(x, y)}")
else:
    print("Invalid operation selected.")
    