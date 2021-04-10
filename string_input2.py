from sys import argv

USAGE = """
用法错误，正确方式如下：
python demo.py one two
"""

if len(argv) != 3:
    print(USAGE)
#    print("debug")
    exit(1)

script, first, second = argv

print("You're running the python scrip: ", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
