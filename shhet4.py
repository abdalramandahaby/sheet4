import random

def generate_password(length, chars):
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password
print(generate_password(8, "abcde"))