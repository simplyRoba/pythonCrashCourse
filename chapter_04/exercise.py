
# 4-1
pizzas = ['Chicago style', 'Boston', 'Hawaii']
for pizza in pizzas:
    print(f"I like {pizza} pizza")
print("I really love pizza!")

# 4-2
pets = ['Dog', 'Cat', 'Bird']
for pet in pets:
    print(f"A {pet} would make a great pet!")

# 4-3
for value in range(1, 21):
    print(value)

# 4-4
a_lot_of_numbers = range(1, 1_000_001)
# for number in a_lot_of_numbers:
#     print(number)

# 4-5
print(min(a_lot_of_numbers))
print(max(a_lot_of_numbers))
print(sum(a_lot_of_numbers))

# 4-6
for odd_number in range(1, 21, 2):
    print(odd_number)

# 4-7
for n in range(1, 31, 3):
    print(n)

# 4-8
cubes = []
for n in range(1, 11):
    cubes.append(n**3)
for cube in cubes:
    print(cube)

# 4-9
cubes = [n**3 for n in range(1, 11)]
for cube in cubes:
    print(cube)

# 4-10
numbers = range(1, 101)

print("The first three items in the list are:")
for n in numbers[:3]:
    print(n)

print("Three items from the middle of the list:")
for n in numbers[56:59]:
    print(n)

print("The last three items in the list are:")
for n in numbers[-3:]:
    print(n)

# 4-11
friend_pizzas = pizzas[:]
pizzas.append("Chicago style Halal")
friend_pizzas.append("Double Peperoni")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
