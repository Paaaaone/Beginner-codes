num = 9
i = 0
while i < 3:
    guess = int(input('Guess: '))
    if guess == num:
        print('Correct')
        break
    elif guess != num:
        i = i+1   