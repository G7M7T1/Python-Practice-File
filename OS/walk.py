import os

for folder, sub_folders, files in os.walk("other"):
    print("--------------------------------------")
    print("Currently we are looking at folder " + folder)
    print("The Subfolders in current directory are:")
    for sub in sub_folders:
        print(sub)

    print("The Files in the current directory are:")
    for file in files:
        print(file)
