import os
import sys

name = input("Enter directory name: ")
os.mkdir(name)
print("Directory created:", name)

file = input("Enter file name: ")
open(file, "w").close()
print("File created:", file)

print("Files:", os.listdir())
print("Python version:", sys.version)
