import random

n = int(input("Enter the number of random numbers to generate: "))

print("Random numbers:")

for i in range(n):
    num = random.randint(1, 100)
    print(num)
