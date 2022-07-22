import os

for root, dirs, files in os.walk("other"):
    for f in files:
        file_name, file_type = os.path.splitext(f)
        if file_type == ".html":
            print(f)
            os.remove(os.path.join(root, f))
