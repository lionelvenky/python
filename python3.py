#lists

#sum

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = sum(numbers)
print("Sum of elements:", sum_of_numbers)

# finding even number

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)



# list manipulation

fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
fruits.insert(1, 'grape')
fruits.remove('banana')
print("Modified list:", fruits)
