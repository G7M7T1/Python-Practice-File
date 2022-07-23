import csv

with open("other.csv", mode="w", newline="", encoding="utf8") as f:
    csv_write = csv.writer(f, delimiter=",")
    csv_write.writerow(["a", "b", "c", "d"])

with open("next.csv", mode="a", newline="", encoding="utf8") as f:
    csv_write = csv.writer(f, delimiter=",")
    csv_write.writerows([["Key 1", "Key 2", "Key 3", "Key 4"], ["Key 5", "Key 6", "Key 7", "Key 8"]])
