"""
Description: Module 02 demonstration
Author: Jashanpreet Singh
Date: September 09, 2024
Usage: To demonstrate content from Module 02.
"""

# This is a single line comment

"""
This is a multi line comment
it can span over multiple lines
"""

absolute_value = abs(-12)

print('Absolute Value:', absolute_value)

print("Absolute Value;", abs(-12))

print("I am", 69, "years old.")
print("I am 69 years old.")

print("apple", "mango", "watermelon")
print("apple", "mango", "watermelon", sep = ",")
print("apple", "mango", "watermelon", sep = " ")

print()
print("print using f-string")
name= "JashanOG"
age= 69

print("My name is", name, "and I am", age, "years old")
print(f"My name is {name} and I am {age} years old")

value= 6969.9696
print("the value is", value)
print("the value is {value:.2f}")

number= 123
print("The number is {number:05}.")

print(f"Hello, {name}")
print(f"Hello, {name:>10}")