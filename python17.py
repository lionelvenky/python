# tuples

#unpacking tuples
coordinates = (3, 4)
x, y = coordinates
print("x =", x)
print("y =", y)


#tuple concatenation

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)


#tuple as dictionary key

name_and_age = {('venky', 25): 'cricket', ('leo', 30): 'football'}
for key, value in name_and_age.items():
    print(key, "-", value)
