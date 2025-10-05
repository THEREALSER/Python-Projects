import re

phone = input("Enter phone number: ")

new_phone_number = re.sub(r'^(?:\+98|0098)', '0', phone)

print("Your phone number is: ", new_phone_number)

