def anagram(s1, s2):
    cor_s1 = s1.replace(" ", "").lower()
    cor_s2 = s2.replace(" ", "").lower()
    sort_s1 = sorted(cor_s1)
    sort_s2 = sorted(cor_s2)
    if sort_s1 != sort_s2:
        return False
    else:
        return True


s1 = input('input first string: ')
s2 = input('input second string: ')
if len(s1) != len(s2):
    print(False)
    exit()
ana = anagram(s1, s2)
print(ana)
