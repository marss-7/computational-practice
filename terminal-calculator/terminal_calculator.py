import math

# Dictionaries for given operations.
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Error: divide by zero",
    "**": lambda a, b: a ** b
}

special_ops = {
    "!": lambda a: math.factorial(int(a)),
    "sqrt": lambda a: math.sqrt(a) if a>=0 else "Root doesn't work with negative numbers."
}

repeat = True

# Main program loop
while repeat == True:
    # Ask for input
    operator = input("Enter one of the following operators: +, -, *, /, !, **, sqrt   ")
    #Take the numbers and print the result of the operation.
    if operator in ["+", "-", "*", "/", "!", "**", "sqrt"]:
        if operator in ["!", "sqrt"]:
            num_1 = float(input("Enter the number: "))
            result = special_ops[operator](num_1)
            print(f"{num_1} {operator} = {result}")
        else:
            num_1 = float(input("Enter the first number: "))
            num_2 = float(input("Enter the second number: "))
            result = operations[operator](num_1, num_2)
            print(f"{num_1} {operator} {num_2} = {result}")
        # Ask if the user wants to continue.
        rep = input("Do you want to continue? Press q to quit.  ")
        if rep.lower() == "q":
            repeat = False
    else:
        print("Invalid operator. Try again. ")