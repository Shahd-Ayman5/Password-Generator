import random
import string

x = True
while x :
    try :
        length_str = input("Enter the desired length of the password, it should be between 6 and 12\n")
        length = int(length_str)
        if length < 6 :
            print("Invalid input. ")
        elif length > 12 :
            print("Invalid input. ")
        else :
            x = False
    except ValueError :
            print("Invalid input. ")

password = []
i = 0
characters = string.ascii_letters + string.punctuation + 10*string.digits
while i < length :
    password.append(random.choice(characters))
    i+=1

print(*password, sep='')
