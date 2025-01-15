import random # I'm importing a library that allows random number generation.
import string # I'm importing a library with digits, letters, punctuation, etc.

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
chars = string.punctuation

# What I've done here is defined the variables of this generator, giving each variable their own library. For example,
# the 'lowercase' variable is now assigned to the lowercase ascii library, which means that it essentially allows that variable
# to mean 'all ascii lowercase letters'.

all_characters = lowercase + uppercase + digits + chars
# I'm combining all the sets into one in order to fill the password with random characters, which allows us to avoid a lot of unnecessary code.

password_length = int(input("enter password length here:"))
# Allows the user to choose what length they want their password to be.

password = [
    random.choice(lowercase), random.choice(uppercase), random.choice(digits), random.choice(chars)
]


for _ in range (password_length - 4):
    password.append(random.choice(all_characters))
# Since there are already 4 characters selected (digits,chars,etc), we need to fill out the rest of the password, this is what this section does.


random.shuffle(password)
# Shuffles the password up for extra randomness.

final_password = ''.join(password)
# Puts the output of the operation into a string.

print("Password created:", final_password)
# Spits out the output of the string with "password created".