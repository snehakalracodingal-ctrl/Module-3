def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
print("Please use this calculator module for basic arithmetic operations.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operation=input("Choose an operation (a/b/c/d): ")
if operation=='a':
    print("The sum is:", add(num1, num2))   
elif operation=='b':
    print("The difference is:", subtract(num1, num2))
elif operation=='c':
    print("The product is:", multiply(num1, num2))
elif operation=='d':
    print("The quotient is:", divide(num1, num2))
else:
    print("Invalid operation selected.")