import re
import os

with open("researchpaper.txt", encoding="utf8") as file:
    text = file.read()
    x = re.findall(r"\([A-Za-z0-9\s]+, \d{4,}\)", text)
    print(x)

path_lst = []
for root, dirs, files in os.walk("Employee"):
    for f in files:
        file_name, file_type = os.path.splitext(f)
        if file_type == ".txt":
            path_lst.append(os.path.join(root, f))

all_number = []
for n in range(0, len(path_lst)):
    with open(path_lst[n], encoding="utf8") as file:
        text = file.read()
        x = re.findall(r"\d{3}-\d{3}-\d{4}", text)
        all_number.append(x)

print(all_number)
