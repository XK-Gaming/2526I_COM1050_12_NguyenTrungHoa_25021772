#W4A11
n = int(input("Enter number: "))
count = 0
for i in range(2, n + 1, 2):
    if n % i == 0:
        count += 1
print(count)