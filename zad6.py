
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "cant divide by zero"
    return a / b

print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

op = input("Please enter choice (a/b/c/d): ").lower()

num1 = int(float(input("Enter first number: ")))
num2 = int(float(input("Enter second number: ")))

if op == 'a':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif op == 'b':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif op == 'c':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif op == 'd':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("invalid option")
