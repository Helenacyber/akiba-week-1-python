
# TASK 1 – Personal Introduction

# Practice variables, strings, and user input.
# Create a program that asks the user for:
# Full name
# Age
# City
# University
# Department
# Favorite programming language
# One programming goal
# Display the



from os import name


print("=" * 40)
print("STUDENT INTRODUCTION")
print("=" * 40)
print()


# Ask for user input
full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
university = input("Enter your university: ")
department = input("Enter your department: ")
fav_language = input("Enter your favorite programming   language: ")
programming_goal = input("Enter your programming goal: ")

# Display the information as a professional introduction
print()
print("=" * 40)
print("STUDENT INTRODUCTION")
print("=" * 40)
print()
print(f"My name is {full_name}.")
print(f"I am {age} years old.")
print(f"I live in {city}.")
print(f"I study {department} at {university}.")
print(f"My favorite programming language is {fav_language}.")
print()
print("My programming goal:")
print(programming_goal)
print()
print("=" * 40)