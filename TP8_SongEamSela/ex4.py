import csv
from textblob import TextBlob


csvData = []

with open('testData.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        csvData.append(row)


with open('testData_result.csv', 'w') as file:
    for data in csvData:
        analysisPol = TextBlob(str(data)).polarity
        analysisSub = TextBlob(str(data)).subjectivity

        writer = csv.writer(file, delimiter=',')
        writer.writerow([analysisPol, data])