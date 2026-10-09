import shutil
import os

src = input("Enter source file: ")

if os.path.exists(src):
    copy = input("Enter copy file name: ")
    shutil.copy(src, copy)
    print("File copied")

    new = input("Enter new file name: ")
    shutil.move(copy, new)
    print("File moved")

    delete = input("Enter file to delete: ")
    if os.path.exists(delete):
        os.remove(delete)
        print("File deleted")
    else:
        print("File not found")
else:
    print("Source file not found")
