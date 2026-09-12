# Exercise 5: The Spy's Word Reverser
def The_Spy_Word_Reverser():
    decrypt_message = input("Enter the Decrypt msg you want to encrypt: ")
    decrypt_message = decrypt_message.split(" ")
    encrypted_message = [i[::-1] for i in decrypt_message]
    encrypted_message = " ".join(encrypted_message)
    print(encrypted_message)


The_Spy_Word_Reverser()
