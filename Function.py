import upper as upper

name = input('Enter name: ')
decision = input('(G)reet or (R)everse? ')

def greet_user(name):
    print("Hello " + name)


def reverse_name(name):
    list_name = list(name)
    rname = list(reversed(list_name))
    rev_name = str().join(rname)
    print(rev_name)


if decision.upper() == 'G':
    greet_user(name)
elif decision.upper() == 'R':
    reverse_name(name)
else:
    print('Invalid input')