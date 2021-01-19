import re

while True:
    text = input("Enter a phone Number: ")
    if len(text) == 9 or len(text) == 10:

        if text.startswith('076'):
            pattern2 = "^076[0-9]{7}$"
            test = re.search(pattern2, text)
            if test:
                print("Correct cellcard phone number pattern")
            else:
                print("Invalid number")
        else:
            pattern1 = "^(011|012|017|077|099)[0-9]{6}$"
            test = re.search(pattern1, text)
            if test:
                print("Correct cellcard phone number pattern")
            else:
                print("Invalid number")


    else:
        print("Invalid phone number")