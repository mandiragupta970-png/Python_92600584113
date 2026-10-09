import re

text = input("Enter text: ")

emails = re.findall(r'\S+@\S+', text)
numbers = re.findall(r'\d+', text)

print("Emails:", emails)
print("Numbers:", numbers)
