from string import ascii_lowercase              # Lowercase ASCII characters

cipher = tuple("odaeeuzsftqdgnuoazxvymiumq")    # The cipher
cipher_copy = None                              # This variable holds a copy of the cipher
alpha = tuple(ascii_lowercase)                  # Lowercase ASCII characters
letter_offset = 0

for shift in range(26): # Repeat this 26 times
    cipher_copy = list(cipher)
    cipher_index = 0
    for letter in cipher:
        letter_ord = ord(letter) + letter_offset # Set "letter_ord" to the ASCII value of the letter plus offset
        if letter_ord > ord('z'): # If the "letter_ord" variable is greater than the ASCII value of the lowercase letter z
            letter_ord = letter_ord - 26 # Subtract 26 from "letter_ord"
        cipher_copy[cipher_index] = chr(letter_ord)
        cipher_index = cipher_index + 1
    letter_offset = letter_offset + 1
    print(str(letter_offset)+":\tpicoCTF{"+''.join(cipher_copy)+"}") # Prints "offset: [tab] picoCTF{cracked_cipher}"
