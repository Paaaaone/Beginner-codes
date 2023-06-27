def check(par):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for p in par:
        if p in mapping:
            if not stack or stack.pop() != mapping[p]:
                return False
        else:
            stack.append(p)
    if len(stack) == 0:
        return True


par = input('Enter parentheses: ')
ans = check(par)
print(ans)
