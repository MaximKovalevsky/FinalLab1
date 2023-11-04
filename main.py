import csv
import os
import random

def Show(data, typeOfDisplay='top', rows=5, sepr=','):
    if typeOfDisplay == 'bottom':
        data = data[-rows:]
    elif typeOfDisplay == 'random':
        if rows > len(data):
            rows = len(data)
        data = random.sample(data, rows)

    for row in data:
        print(sepr.join(row))


def Info(data):
    rows = len(data) - 1
    cols = len(data[0])
    print(f"Количество строк с данными: {rows}")
    print(f"Количество колонок в таблице: {cols}")

    header = data[0]
    for colIndex, colName in enumerate(header):
        NotZeroCount = sum(1 for row in data[1:] if row[colIndex] != '')
        typeOfCol = type(data[1][colIndex]).__name__
        print(f"{colName:10} {NotZeroCount:5} {typeOfCol}")


def DelNaN(data):
    for row in data:
        if all(field != '' for field in row):
            return data

def MakeDs(data):
    random.shuffle(data)
    splitIndex = int(0.7 * len(data))
    learningData = data[:splitIndex]
    testingData = data[splitIndex:]

    baseDirectory = os.path.dirname(os.path.abspath(__file__))
    workDirectory = os.path.join(baseDirectory, 'workdata')
    learnDirectory = os.path.join(workDirectory, 'Learning')
    testDirectory = os.path.join(workDirectory, 'Testing')

    os.makedirs(learnDirectory, exist_ok=True)
    os.makedirs(testDirectory, exist_ok=True)

    learnFile = os.path.join(learnDirectory, 'train.csv')
    testFile = os.path.join(testDirectory, 'test.csv')

    write(learnFile, learningData)
    write(testFile, testingData)

def load(path):
    data = []
    with open(path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def write(path, data):
    with open(path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


path = 'data.csv'

data = load(path)

Show(data, typeOfDisplay='top', rows=5, sepr=',')
print()

Info(data)
print()

data = DelNaN(data)

MakeDs(data)