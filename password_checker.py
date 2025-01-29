#import string module that will check existence for certain characters.
#import time module that will provide varioud time functions. 
import string
import time

#welcome the user: 
print("Hello! Welcome to Jelly's Cyber World!\nI am glad you are here!\nBefore you can enter this world, Please a create a username and password!")

#take username input from user. 
username = input("\nPlease create a username: ")

#open txt file containing common passwords. 
#read the list of passwords from the file. with ensures file is properly closed. 
with open('password_list.txt', 'r') as f: 
    #f.read reads the entire content of the file into a single string.
    #.splitlines() splits the string into a list of lines, where each line corresponds to one entry in the file. 
    common = f.read().splitlines()

#prompt the user to crate a password. 
print(f"\nwelcome {username}! Lets create a password for you!")
password = input("write your password here: ")

#enter a loop until a password that is not in the common txt or length less than 8 is provided: 
while password in common or len(password) < 8:
    if password in common:
        print("Password was found in a common list of passwords, therfore not secure!")
        password = input("Please Enter a another password: ")
    elif len(password) < 8:
        print("Password is too short, please enter minimum 8 characters! :")
        password = input("Please Enter a another password: ")
    else: 
        #break out of the loop
        break 

#Second part of the program, check the complexity. 
#setting a variable to check for uppercase. 
#1 meaning there's uppercase in user's input.
#0 meaning there is no uppercase in user's input.
#any function checks if any iterm in iterable are true, otherwise return false. 
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

#a variable to check if password contains any of the characters. 
characters = [upper_case, lower_case, special, digits]
#count the length of the passsord. 
length = len(password)
#initilise the score. 
score = 0 

time.sleep(2) #pause for 2 seconds. 
#give 1 point if length of password is more than or equal to 8. 
if length >= 8:
    score += 1
print(f"\nPassword length is {str(length)}, adding 1 point.")

time.sleep(2)
# Count the number of character types and add points
num_character_types = sum(characters)
score += num_character_types
print(f"\nPassword has {str(num_character_types)} different character types, adding {str(num_character_types)} points.")

time.sleep(2)
# Evaluate password strength based on the score
if score < 3:
    print(f"\nYour password is quite weak. Score: {score}")
elif 3 <= score <= 4:
    print(f"\nYour password is okay. Score: {score}")
elif score >= 5:
    print(f"\nYour password is pretty good! Score: {score}")

#ending statement
time.sleep(2)
print(f"\nThank you for registering to Jelly's Cyber World {username}!")

tips = """
Here are a few more tips for creating secure passwords!

1) Passwords should have a minimum of 8 characters.
2) Passwords need characters from at least three of the following:
   - Uppercase letters
   - Lowercase letters
   - Non-alphanumeric characters (e.g., @, #, $)
3) Avoid common patterns, such as capital letters at the start and symbols at the end.
   Cyber criminals are aware of such patterns.
4) Do not reuse passwords across multiple accounts. If one gets breached, your other accounts are in danger!
5) Make your password hard to guess by avoiding personal information like your name or birthday.

Finally, add an extra layer of protection with Multi-Factor Authentication (MFA)!

Feel free to run this program again and create more secure passwords! Goodbye.
"""

print(tips)
