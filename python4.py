# sets


#union of sets

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of sets:", union_set)

# common elements

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
common_elements = set_a.intersection(set_b)
print("Common elements:", common_elements)


# removing duplicates

numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers_with_duplicates))
print("List with duplicates removed:", unique_numbers)
