# Dictionaries for given convertions
operations = {
    "1": [lambda a: a * 0.621371, "km", "miles"], #km to miles
    "2": [lambda a: a * 1.60934, "miles", "km"], #miles to km
    "3": [lambda a: a*(9/5) + 32,"C°", "F°"], #celsius to farenheit
    "4": [lambda a: (a-32) * (5/9),"°F", "°C"], ##farenheit to celsius
    "5": [lambda a: a*2.20462,"kg", "pounds"], #kg to pounds
    "6": [lambda a: a*0.453592, "pounds", "kg"] #pounds to kg
}

repeat = True

# Main program loop
while repeat == True:
    #Ask the user for input
    print("What do you want to convert? \n 1. Kilometers to Miles \n 2. Miles to Kilometers \n 3. Celsius to Fahrenheit \n 4. Fahrenheit to Celsius \n 5. Kilograms to Pounds \n 6. Pounds to Kilograms")
    conversion = (input())
    #Take the numbers and print the result of the conversion.
    if conversion in ["1", "2", "3", "4", "5", "6"]:
        num = float(input("Enter the value to convert: "))
        result = operations[conversion][0](num)
        print(f"{num}  {operations[conversion][1]} = {result}  {operations[conversion][2]}")
        # Ask if the user wants to continue.
        rep = input("Do you want to continue? Press q to quit.  ")
        if rep.lower() == "q":
            repeat = False
    else:
        print("Invalid operator. Try again. ")