# mode "r" "a" "w" "x"

# "r" for Read
# "a" for Append
# "w" for write
# "x" for Create

choose = input("Hi, What do you want to do? Add line(1) or Rewrite(2)")
text = input("What Sentence you want to write?")

if choose == "1":
    # Add Line
    with open("myText.txt", mode="a") as my_file:
        my_file.write(text + "\n")
elif choose == "2":
    # Rewrite
    with open("myText.txt", mode="w") as my_file:
        my_file.write(text + "\n")
else:
    print("Please Enter 1 or 2")
