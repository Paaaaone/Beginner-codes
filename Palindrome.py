def isPalindrome(s):
    n = int(len(s))
    for i in range(0, int(n/2)):
        if s[i] != s[n-i-1]:
            return False
        else:
            return True


s = input('Enter string to check: ')
pcheck = isPalindrome(s)
print(pcheck)
