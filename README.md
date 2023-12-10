# Random Password Generator

## Features and Functionality

This Python script generates random passwords based on user input for the desired password length. It combines lowercase letters, uppercase letters, numbers, and special characters to create a diverse and secure password.

### Password Generation Process

- The script uses the `random` module to generate passwords.
  
- Four string variables (`lower_case`, `upper_case`, `numbers`, `special_characters`) store the character sets for different types of characters.

- The `characters` variable concatenates these sets to create a pool of characters from which the password will be generated.

- The script enters a `while` loop, presenting the user with a menu to generate passwords continuously.

- Inside the loop:
  1. The user is prompted to enter the desired character limit for the password.
  2. A password is generated using `random.sample` to select characters randomly from the character pool.
  3. The generated password is displayed to the user.

### User Interaction

- The user is given the option to generate more passwords by entering 'Y' or 'N' in response to the prompt: "Do you want to generate more passwords??[Y/N]".

- If the user chooses 'Y', the loop continues, and a new password is generated.
  
- If the user chooses 'N' or any other input, the script exits the loop and terminates.

### Running the Password Generator

- To use the password generator, execute the script.

- Enter the desired character limit for the password when prompted.

- The generated password will be displayed, and the user can choose to generate more passwords or exit the generator.

### Sample Usage

```python
while True:
    print("---Welcome to Random Password Generator---")
    pass_length = int(input("Enter character limit for password:"))
    password = "".join(random.sample(characters, pass_length))
    print("Your new Password is: ", password)
    ch = input("Do you want to generate more passwords?? [Y/N]")
    if ch == 'y' or ch == 'Y':
        continue
    else:
        break
