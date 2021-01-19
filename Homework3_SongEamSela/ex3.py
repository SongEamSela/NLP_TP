import re
n = input("Please enter the binary number: ")
reg = re.search("^[01]+$", n)
print(reg)