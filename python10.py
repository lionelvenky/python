
# file handling


# write to a file

with open("example.txt", "w") as file:
    file.write("This is a sample text.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)




# exception handling


try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")
