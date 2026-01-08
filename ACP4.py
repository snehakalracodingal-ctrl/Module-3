age = int(input("Enter your age: "))

if age <= 0:
    print("Invalid age")
else:
    if age % 2 == 0:
        print("Valid age and it is even")
    else:
        print("Valid age and it is odd")
