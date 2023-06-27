s1 = input('Enter string: ')
split_s1 = s1.split(" ")
l = len(split_s1)
for i in reversed(range(l)):
    print(split_s1[i], end=" ")
print(" ")
