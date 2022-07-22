import zipfile

zipped_file_1 = zipfile.ZipFile("paper.zip", "w")
zipped_file_1.write("paper.txt", compress_type=zipfile.ZIP_DEFLATED)
zipped_file_1.close()

zipped_file_2 = zipfile.ZipFile("3.zip", "w")
zipped_file_2.write("1.txt", compress_type=zipfile.ZIP_DEFLATED)
zipped_file_2.write("2.txt", compress_type=zipfile.ZIP_DEFLATED)
zipped_file_2.close()

