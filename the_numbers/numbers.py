numbers = (16, 9, 3, 15, 3, 20, 6)
numbers_two = (20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14)

numbers_crack = []
numbers_crack_two = []

for i in numbers:
    numbers_crack.append(chr(i+96))

print(numbers_crack)

for i in numbers_two:
    numbers_crack_two.append(chr(i+96))

print(numbers_crack_two)
