import random

def generate_password(length, chars):
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password
print(generate_password(8, "abcde"))




chars = ''.join([chr(i) for i in range(ord('0'), ord('9')+1)] + 
                [chr(i) for i in range(ord('A'), ord('Z')+1)] + 
                [chr(i) for i in range(ord('a'), ord('z')+1)])

print(chars)









family = ["Ali", "Sara", "Omar", "Mona"]

letters_used = {letter.lower() for name in family for letter in name}

print(letters_used)








def average(*numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return 0 

print(average(10, 20, 30))







def substitute(equation, **kwargs):
    try:
        result = eval(equation, {}, kwargs)
        return result
    except Exception as e:
        return f"Error: {e}"


print(substitute("a + b * 2", a=3, b=4))