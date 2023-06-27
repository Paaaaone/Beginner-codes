number = [int(num) for num in input('Enter numbers with space: ').split()]
max_number = int(max(number))

min_number = int(min(number))
missing = []
for i in range(min_number+1, max_number):
    if i not in number:
        missing.append(i)
print(missing)
