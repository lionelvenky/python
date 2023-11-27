# for loop

for i in range(1, 6):
    print(i)


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


numbers = [1, 2, 3, 4, 5]
sum_result = 0
for num in numbers:
    sum_result += num
print("Sum of numbers:", sum_result)


# while loop

counter = 1
while counter <= 5:
    print(counter)
    counter += 1


num = int(input("Enter a number: "))
factorial_result = 1
while num > 0:
    factorial_result *= num
    num -= 1
print("Factorial:", factorial_result)
