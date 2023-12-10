import random
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_characters = "!@#$%^&*()."

characters = lower_case + upper_case + numbers + special_characters
while True:
    print("---Welcome to Random Password Generator---")
    pass_length = int(input("Enter character limit for password:"))
    password = "".join(random.sample(characters,pass_length))
    print("Your new Password is: ", password)
    ch=input("Do you want to generate more passwords??[Y/N]")
    if ch=='y' or ch=='Y':
        continue
    else:
        break
