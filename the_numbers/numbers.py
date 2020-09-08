numbers = (16, 9, 3, 15, 3, 20, 6) # picoctf
numbers_two = (20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14) # thenumbersmason

numbers_crack = []
numbers_crack_two = []

for i in numbers:
    numbers_crack.append(chr(i+96)) # append the ASCII character of the number plus 96

for i in numbers_two:
    numbers_crack_two.append(chr(i+96)) # like line 8, append the ASCII character of the number plus 96

print(numbers_crack, numbers_crack_two)
