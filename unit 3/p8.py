import re

text = input("Enter text: ")
pattern = input("Enter pattern: ")

if re.match(pattern, text):
    print("Pattern matched")
else:
    print("Pattern not matched")
