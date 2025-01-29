## Code Explaination for Secure Password Checker
This python code will take user’s input and check it against the common passwords text file while also giving it a score depending on how strong it is. 

1. Importing the string module!

```python
import string
import time
```

- Lets import the string module. This module will allow us to check if the password contains certain types of character (e.g., uppercase letters, digits, special characters, etc.).
- We are also going to use the time modules where we can utilise various time-related functions.
2. Welcome the user. 

```python
print("Hello! Welcome to Jelly's Cyber World!\nI am glad you are here!\nBefore you can enter this world, Please create a username and a password!")

```

- Here is our simple message welcoming the user to our hypothetical website.
- The print function in python will print your message to the user.
    - In this case, it will print the the string indicated by “” inside the brackets.
- The “\n” escape character will insert line breaks within the string. This is added to make the message appear in a clean manner to the user.

3. Lets ask the user to create a username. 

```python
username = input("\nPlease create a username: ")
```

- Here we have a variable called “username.” You can think of variables like a container that holds value you can use later on in the program. For example, the “username” variable might store the name “John.”
- But in this program, we want the user to choose their own username! So that is where the **input()** function comes in. This function will take input from the user. In this case we are asking the user to enter a username.
- Whatever the user entered will now be stored in our variable “username” that we can later call open.
- The “\n” escape character used in this piece of code is to just keep the code clean.
4. Reading the list of common passwords. 

```python
with open('password_list.txt', 'r') as f:
    common = f.read().splitlines()
```

- Here, we will be dealing with files.
    - The password_list.txt is a file that I have in my computer composed of 100,000 common password as provided by [ncsc.gov.uk](http://ncsc.gov.uk). Here is the link if you’re interested: https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt.
    - You can create your own txt file and add other common passwords if you’d like.
- The **with open()** statement is used to open the file “password_list.txt” in reading mode.
- The **f.read()** will read the entire file and the **splitlines()** will split the strings into a list of lines, where each line becomes an element in the list.
- The common variable will store the list of lines from the file. This means each line in the file will be an item in the common list.
- Here is an simple view of what is happening:
    - here we have a txt file containing these three common passwords.

```
password123
123456
qwerty
```

- After running the code, the common variable would look something like this:

```python
['password123', '123456', 'qwerty']
```

- This allows us to work with each password in the list individually.

5. Ask the user to create a password. 

```python
print(f"\nwelcome {username}! Lets create a password for you!")
password = input("write your password here: ")
```

- Here, we are welcoming the user by using the  variable “username” which contains the input they provided earlier in the program. We are using an f-string which allows us to easily insert the value of a variable in the string.
- In the next line, we are using the **input ()** to prompt the user to enter a password and storing it in a variable called “password.”
6. Creating a while loop

```
 while password in common or len(password) < 8:
    if password in common:
        print("Password was found in a common list of passwords, therfore not secure!")
        password = input("Please Enter a another password: ")
    elif len(password) < 8:
        print("Password is too short, please enter minimum 8 characters! :")
        password = input("Please Enter a another password: ")
    else: 
        break
```

- We want to prompt the user to enter password again if it is found in the common list of passwords or if their password do not reach the minimum length required.
- Out of the two primitive loop commands in python, we will use the While loop. This loop will execute set of statements as long as a condition is true.
7. Checking for character types: 

```python
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

```

- In this part of the code, we create variables to check if the password contains any of the following character types: uppercase letters, lowercase letters, special characters, and digits.
    - The code iterates through each character (c) in the password to check for these character types.
- The any() function checks if at least one element in the list is True. For example, if there is at least one uppercase letter, the upper_case variable will be set to True. This is done by the list comprehension generating a list of 1s (for matches) and 0s (for non-matches).
    - The any() function simplifies the list of 1s and 0s by returning True if at least one 1 is found, meaning the condition is met, and False if none of the conditions are met.
8. Storing Character Type Checks in a list: 

```python
characters = [upper_case, lower_case, special, digits]
```

- Here, we are storing the results of the checks (whether the password has upper_case, lower_case, special, and digits) as a list in a variable called the “characters.”
- You can run the code you have so far and experiment to check the program is running as intended by putting in:

```python
print(characters)
```

- Here is my result for the password “jelly”: [False, True, False, False].
    - As you can see, I do not have any uppercase, special character or digits as indicated by False.
    - My password only contains lowercase characters as indicated by True in the list.
- You may delete the print(characters) once you are done experimenting.
9. Getting the password length. 

```python
length = len(password)
```

- we are creating another variable named “length.” As the name suggest we are going to store the number of characters in the password by using the **len()** function.
10. Initialising score

```python
score = 0 
```

- A score variable is initialised with 0. This score will increase based on the strength based on the strength of the password as evaluated later in the code.
11. Utilising time.sleep () function: 

```python
time.sleep(2)
```

- This is the time.sleep() function. The number inside means that I want the program to pause for 2 seconds before executing the next lines of code.
- I am using this feature to not overwhelm the user and give more natural flow to the program.
- You can use this as you see fit throughout your program.
12. Evaluating Password Length: 

```python
if length >= 8:
    score += 1
print(f"\nPassword length is {str(length)}, adding 1 point.")
```

- Here we are using if statements where if the length of the password is more than or equal to 8, we will give user 1 point.
- The str(length) converts the length of the password to a string.
13. Evaluating Character Variety:

```python
num_character_types = sum(characters)
score += num_character_types
print(f"\nPassword has {str(num_character_types)} different character types, adding {str(num_character_types)} points.")
```

- Create a new variable “num_character_types” which will store the sum of the characters.
- Score given to the user will depend on how many variety of characters they have in their password. For example, if their password contains upper_case and lower_case only, that is 2 points.
- Last code prints how many character types were found in user’s password and the number of score they earned.
14. Number of points earned: 

```python
if score < 3:
    print(f"\nYour password is quite weak. Score: {score}")
elif 3 <= score <= 4:
    print(f"\nYour password is okay. Score: {score}")
elif score >= 5:
    print(f"\nYour password is pretty good! Score: {score}")
```

- We are calculating the total score and corresponding it with how secure their password is.
- If their total score is less than 3, their password is quite weak and so on.
15. Giving advice on creating secure passwords:

```python
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
```

- Finally, we are ending our program by giving advice for the user on creating secure passwords.

That’s the end, thank you for reading if you stuck around! Here are some resources I used to help me create this program: 

- https://www.youtube.com/watch?v=iJ01q-sRJAw
- https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt
- https://learn.microsoft.com/en-us/microsoft-365/admin/misc/password-policy-recommendations?view=o365-worldwide
