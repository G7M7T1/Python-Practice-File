import os

# Current locate
print(os.getcwd())

print(os.listdir(os.curdir))

print(os.listdir(os.pardir))

print(os.path.join("folder", "hello.txt"))

os.rename("a.txt", "a.txt")

os.mkdir("New Folder")

os.removedirs("New Folder")