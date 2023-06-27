j = int(input("Number of rows: "))
i = 1
n = j-i
while i <= j:
    print(n * " ", i * "*")
    i = i + 2
    n = n - 1