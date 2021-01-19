import re

while True:
    text = str(input("Enter a phone Number: "))
    if len(text) == 9 or len(text) == 10:
        pattern1 = "^0[10|15|69|70|86|93|98]([0-9]{6})$"
        pattern2 = "^096[0-9]{7}$"
        test1 = re.match(pattern1, text)
        test2 = re.match(pattern2, text)
        print(test2,test1)
        if test1:
            print("Correct Smart phone number pattern")
        elif test2:
            print("Correct Smart phone number pattern")
        else:
            print("Invalid number")
    else:
        print("Invalid phone number")