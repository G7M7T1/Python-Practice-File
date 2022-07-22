import sys


def main():
    contents = sys.stdin.read()
    new_contents = contents.replace(sys.argv[1], sys.argv[2])
    sys.stdout.write(new_contents)


main()

# python ssp.py zero 0 < text.txt > out_text.txt
# > means to overwrite
# >> means to append
# < means to read
