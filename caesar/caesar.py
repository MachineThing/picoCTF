from string import ascii_lowercase

cipher = tuple("odaeeuzsftqdgnuoazxvymiumq")
cipher_copy = None
alpha = tuple(ascii_lowercase)
letter_index = 0

for shift in range(26):
    cipher_copy = list(cipher)
    cipher_index = 0
    for letter in cipher:
        letter_ord = ord(letter) + letter_index
        if letter_ord > ord('z'):
            letter_ord = letter_ord - 26
        cipher_copy[cipher_index] = chr(letter_ord)
        cipher_index = cipher_index + 1
    letter_index = letter_index + 1
    print(str(letter_index)+":\tpicoCTF{"+''.join(cipher_copy)+"}")
