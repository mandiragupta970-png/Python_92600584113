import re

text = input("Enter text: ")
pattern = input("Enter pattern: ")

print("Match:", re.match(pattern, text))
print("Search:", re.search(pattern, text))
print("Findall:", re.findall(pattern, text))
