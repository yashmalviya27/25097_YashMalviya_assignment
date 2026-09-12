# Exercise 6: Shift Cipher Encrypter
def shift_cipher_encrypter():
    data = input("Enter data: ")
    result = "".join(chr(ord(char) + 3) for char in data)
    print(result)


shift_cipher_encrypter()