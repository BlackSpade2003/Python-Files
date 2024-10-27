import random as rd

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '|', '/ ' , '< ', '>', '?']
numbers = ['0', '1', '2', '3', '4', '5','6', '7', '8', '9']

total_alphabet = int(input("How many characters to be in password: "))
total_symbls = int(input("How many symbols to be in password: "))
total_numbers = int(input("4How many numbers to be in password: "))

# Generate password
password =""
# Generate password list form random choices
password_list = []

# Add alphabets
for i in range(0, total_alphabet):
    password_list.append(rd.choice(alphabets))
#Add Symbols
for i in range(0, total_symbls):
    password_list.append(rd.choice(symbols))
#Add Numbers
for i in range(0, total_numbers):
    password_list.append(rd.choice(numbers))

#Password List before Shuffling
print(password_list)

rd.shuffle(password_list)

#Password List after Shuffling
print(password_list)

# Convert password list to string
for char in password_list:
    password += char

# Print Password
print(password)