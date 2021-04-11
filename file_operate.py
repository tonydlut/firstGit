"""
    name: file_operate.py
    Version: 1.0
    Author: Jimmy
    Date: 2021-04-10
    This python is for string input test
"""
import sys, os


def copy_file(src_file, des_file):
    """
    Function to copy file from srcFile to desFile
    """
    isexist = os.access(src_file, os.F_OK)
    isreadable = os.access(src_file, os.R_OK)
    iswritable = os.access(src_file, os.W_OK)

    if not isExist:
        print("%s does not exit" % src_file)
        exit(1)

    if not isReadable:
        print("%s cannot read. Exit" % src_file)
        exit(1)

    if not iswritable:
        print("%s cannot write. Exit" % des_file)
        exit(1)

    print("Copying to %s from %s..." % (des_file, src_file))
    src_file_handler = open(src_file, 'r')
    des_file_handler = open(des_file, 'w')

    try:
        des_file_handler.write(src_file_handler.read())
        print("Finish copying")
        return 0
    except Exception as e:
        print("Failed to copy file : %s" % e)
        exit(1)
    finally:
        des_file_handler.close()
        src_file_handler.close()


USAGE = """
用法错误，正确方式如下：
python3 file_operate.py <filename> <filename>
"""

if len(sys.argv) != 3:
    print(USAGE)
    #    print("debug")
    exit(1)

filename = sys.argv[1]

isExist = os.access(filename, os.F_OK)
isReadable = os.access(filename, os.R_OK)

if not isExist:
    print("%s does not exit" % filename)
    exit(1)

if not isReadable:
    print("%s cannot read. Exit" % filename)
    exit(1)

content = open(filename, 'r')

print("The file your open is %s:" % filename)
print("file content from %s are:" % filename)

print(content.read())
content.close()


copy_file(sys.argv[1], sys.argv[2])

