"""
    Version: 1.0
    Author: Jimmy
    Date: 2021-04-09
    This python is for string input test
"""
print("What's your name?"),
name = input()

print("How old are you?"),
age = input()

# print("Hello, $s, you have been $r years old, please work harder" % (name, age))
"""
error from above code:
Traceback (most recent call last):
  File "F:/Dev_Tools/Pycharmproject/day1/string_input.py", line 13, in <module>
    print("Hello, $s, you have been $r years old, please work harder" % (name, age))
TypeError: not all arguments converted during string formatting
"""

print("Hello, %s, you have been %s years old, please work harder" % (name, age))

print(isinstance(age, int))

age = int(age)

print(isinstance(age, int))
