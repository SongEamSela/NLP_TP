import re

while True:
    text = str(input("Input year: "))
    pattern = "(20[2-9][0-9])|(2[1-9][0-9][0-9])|([3-9][0-9][0-9][0-9])"
    test = re.match(pattern, text)
    if test:
        print("Correct Input")
        break
    else:
        print("Wrong Input")