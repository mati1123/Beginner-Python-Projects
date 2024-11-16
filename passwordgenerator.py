
# Write your solution here
import random
import string

def generate_strong_password(amount:int,include_numbers: bool, include_special: bool):
    password_list = []

    if include_numbers:
        password_list.append(random.choice(string.digits))

    # Steg 4: Lägg till specialtecken om `include_special` är True
    if include_special:
        password_list.append(random.choice("!?=+-()#"))
        
    while len(password_list) < amount:
        passwords = random.choice(string.ascii_lowercase)

        password_list.append(passwords)

    random.shuffle(password_list)
    return ''.join(password_list)


for i in range(10):
    print(generate_strong_password(8, True, True))
