# multiple exceptions

try:
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    result = num1 / num2
    print("Result:", result)
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)



#custom exceptions

class NegativeNumberError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise NegativeNumberError("Age cannot be negative.")
    print("Your age is:", age)
except NegativeNumberError as e:
    print("Error:", e)


# file not found  exceptions

try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Check the file path.")
