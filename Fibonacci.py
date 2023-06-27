n = int(input('Enter number: '))
r = [0] * (n+2)
r[0] = 1
r[1] = 1
for i in range(2):
    print(r[i])
for i in range(2, n):
    r[i] = r[i-1] + r[i-2]
    print(r[i])
