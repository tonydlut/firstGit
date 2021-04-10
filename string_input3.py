"""
    name: string_input3.py
    Version: 1.0
    Author: Jimmy
    Date: 2021-04-09
    This python is for string input test
"""
import sys

USAGE = """
用法错误，正确方式如下：
python3 demo.py one two
"""

if len(sys.argv) != 3:
    print(USAGE)
    #    print("debug")
    exit(1)

print("You're running the python scrip: ", sys.argv[0])
print("Your first variable is:", sys.argv[1])
print("Your second variable is:", sys.argv[2])
