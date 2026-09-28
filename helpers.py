# Import the math module
import math


# Create a function that returns a welcome message
def welcome(name):
    return f"Welcome to PLP, {name}!"


# Create a function to calculate the number of tables needed
def tables_needed(people, seats_per_table):
    return math.ceil(people / seats_per_table)


# Run this code only when helpers.py is run directly
if __name__ == "__main__":
    print(tables_needed(12, 4))