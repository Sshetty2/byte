def likes(names):
    if len(names) == 0:
        print('no one likes this')
    if len(names) == 1:
        print(f'{names[0]} likes this')
    if len(names) == 2:
        print(f'{names[0]} and {names[1]} like this')
    if len(names) == 3:
        print(f'{names[0]}, {names[1]} and 1 other person likes this')
    if len(names) > 3:
        print(f'{names[0]}, {names[1]} and {len(names)-2} other people like this')

print(likes(["Max", "John", "Mark"] ))