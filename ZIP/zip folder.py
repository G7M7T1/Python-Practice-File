import shutil

# zip
folder_zip = "D:\\Python\\Python-Practice-File\\ZIP\\Employee"
out_name = "D:\\Python\\Python-Practice-File\\ZIP\\out"
shutil.make_archive(out_name, "zip", folder_zip)

# unzip
folder_unzip = "D:\\Python\\Python-Practice-File\\ZIP\\out.zip"
unzip_name = "D:\\Python\\Python-Practice-File\\ZIP\\result"
shutil.unpack_archive(folder_unzip, unzip_name, "zip")