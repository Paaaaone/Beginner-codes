string = input('Enter string: ')
char_list = list(string)
reverse = [None] * len(char_list)
n = len(char_list)
for i in range(n):
    reverse[i] = char_list[n-i-1]

char_list = "".join(reverse)
print(char_list)
