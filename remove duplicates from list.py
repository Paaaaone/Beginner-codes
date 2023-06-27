numbers = [2, 5, 32, 5, 6, 2, 6, 7, 9, 75, 45, 45, 3]
unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)
print(unique)