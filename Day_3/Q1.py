"""
Write a program that works out whether if
 a given number is an odd or even number."""

# Which number do you want to check?
number = int(input())

# If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
  print("This is an even number.")
# Otherwise (number cannot be divided by 2 with 0 remainder).
else:
  print("This is an odd number.")