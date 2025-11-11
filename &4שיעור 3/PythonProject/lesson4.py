import csv
import json


def GetPath(path):
    with open(path, 'r') as file:
        content = file.read()
    return len(content.split())


print(GetPath("a.txt"))


def func(lists):
    with open('people.csv ', 'w') as csvfile:
        write = csv.writer(csvfile)
        for row in lists:
            write.writerow(row)


func([["chany", "Coen", "me", 19], ["chany", "Coen", "me", 19], ["chany", "Coen", "me", 19]])


def ex3(d: object) -> object:
    with open("data.json", "w") as jsonfile:
        json.dump(d, jsonfile)

    with open('data.json', "r") as jsonfile:
        data2 = json.load(jsonfile)
        print(data2)


d = {"1": 1, "2": 2, "3": 3}
ex3(d)
