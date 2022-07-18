from sys import argv

if len(argv) < 2:
    print("Please give a File Name")
else:
    file = open(argv[1])
    lines = file.read()
    lines = lines.split("\n")
    line_count = len(lines)
    print(f"The Line count: {line_count}")

    word_count = 0
    char_count = 0
    for line in lines:
        words = line.split(" ")
        word_count += len(words)
        char_count += len(line)
    print(f"The Words count: {word_count}")
    print(f"The Letter count: {char_count}")

    print(lines)

# python read.py XXXXX.txt
