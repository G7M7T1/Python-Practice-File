import zipfile

zipped_obj = zipfile.ZipFile("3.zip", "r")
zipped_obj.extractall("unzip")
zipped_obj.close()