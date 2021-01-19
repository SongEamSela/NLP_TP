import re
n = input('Enter the hexadecimal number: ')
reg = re.search("^[1-9A-Fa-f]+$", n)
print(reg)