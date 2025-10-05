import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+', '=']


print("Welcome to password for lazy people")
nr_letters = int(input("How many letters would you like to be in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like to be in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like to be in your password?\n"))
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
