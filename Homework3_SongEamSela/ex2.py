import re
w = input("Enter a word: ")
reg = re.search("^ch.*e$",w)
print(reg)