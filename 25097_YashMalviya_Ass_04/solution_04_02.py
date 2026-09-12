# contacts = {}


# def register_contact(contacts, name, phone_input):
#     try:
#         if not name.isalpha():
#             raise ValueError("Name should contain only alphabets.")

#         if not phone_input.isdigit():
#             raise ValueError("Phone number should contain only digits.")

#         if len(phone_input) != 10:
#             raise ValueError("Phone number must contain exactly 10 digits.")

#         contacts[name] = phone_input

#         print("Contact registered successfully!")
#         print(contacts)

#     except ValueError as ex:
#         print(f"The error is: {ex}")


# register_contact(contacts, "yash", "1234567890")


class InvalidPhoneNumberError(Exception):
    pass


contacts = {}


def register_contact(phonebook, name, phone_input):
    if (
        not isinstance(name, str)
        or not name.strip()
        or not all(char.isalpha() or char == " " for char in name)
    ):
        raise ValueError("Contact name must be a non-empty alphabetic string.")
    try:
        int(phone_input)
    except ValueError:
        raise InvalidPhoneNumberError("Phone number must contain digits only.")

    # Store phone number as string
    phonebook[name] = phone_input

    return phonebook


# 1. Valid Input
contacts = register_contact(contacts, "Alice", "0987654321")
print(contacts)


# 2. Invalid Phone Number
try:
    contacts = register_contact(contacts, "Bob", "123-456-789")
except InvalidPhoneNumberError as e:
    print(e)


# 3. Invalid Name
try:
    contacts = register_contact(contacts, "Bob123", "9876543210")
except ValueError as e:
    print(e)
