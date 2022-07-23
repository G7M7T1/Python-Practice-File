import csv

with open("file.csv", newline="", encoding="utf8") as f:
    csv_data = csv.reader(f)

    for line in csv_data:
        print(line)