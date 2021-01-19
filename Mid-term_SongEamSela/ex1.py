from datetime import date

birthdate = input("Enter your birthdate in formath 'day month year' or 'dd MM yyyy: ")

spcae = 0
isCorrectFormat = False
isCorrectDate = False
day = 0
month = 0
year = 0
dateList = []
today = date.today()

for i in range(0, len(birthdate)):
    if birthdate[i] == " ":
        spcae = spcae + 1

if spcae == 2:
    isCorrectFormat = True
    dateList = birthdate.split(" ")
else:
    print("You have Inputed wrong date format")

if isCorrectFormat:
    for i in range(0, len(dateList)):
        if i == 0:
            day = int(dateList[i])
        elif i == 1:
            month = int(dateList[i])
        elif i == 2:
            year = int(dateList[i])

    if day > 0 and day <= 31:
        if month > 0 and month <= 12:
            if year > 1000 and year < int(today.strftime("%Y")):
                isCorrectDate = True
            elif year > int(today.strftime("%Y")):
                print("You inputed year bigger than current year")
            else:
                print("You inputed too small number of year")
        else:
            print("you inputed invaild month")
    else:
        print("You inputed invaild date")

if isCorrectDate:
    total_year = 100
    total_hour = ((365 * 24) + 6) * total_year

    past_year = int(today.strftime("%Y")) - year

    d = int(today.strftime("%d")) - day
    m = int(today.strftime("%m")) - month
    # suppose that 1 month is 30 days
    past_hour = (((365 * 24) + 6) * past_year) + (d * 24 + ((m * 30) * 24))

    total_remain_hour = total_hour - past_hour

    remain_year = int(total_remain_hour / ((365 * 24) + 6))
    remain_month = int((total_remain_hour % ((365 * 24) + 6)) / (30 * 24))
    remain_day = int((total_remain_hour % ((365 * 24) + 6)) % (30 * 24) / 24)
    remain_hour = int((total_remain_hour % ((365 * 24) + 6)) % (30 * 24) % 24)
    remain_min = 60 - int(today.strftime("%M"))

    print("Remain life time of a person is : " + str(remain_day) + "days," + str(remain_month) + "months," + str(
        remain_year) + "years," + str(remain_hour) + "h:" + str(remain_min))

