# Import the random module to generate random characters
import random

# Import the string module to use letters and numbers
import string


# Create a function to generate a password
# The default password length is 8 characters
def make_password(length=8):
    # Create a collection of letters and numbers
    characters = string.ascii_letters + string.digits

    # Start with an empty password
    password = ""

    # Repeat the process according to the required password length
    for i in range(length):
        # Add one random character to the password
        password += random.choice(characters)

    # Return the completed password
    return password


# Generate an 8-character password using the default length
p1 = make_password()

# Generate a 12-character password
p2 = make_password(12)


# Print the first password and its length
print("Password:", p1)
print("Length:", len(p1))

# Print the second password and its length
print("Password:", p2)
print("Length:", len(p2))