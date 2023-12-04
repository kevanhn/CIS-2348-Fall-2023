# Kevin Nguyen 1928145

parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))
        parts = input().split()
        name = parts[0]
        if age == 'Beth':
            age = 0

    except ValueError as excpt:
        age = 0
        print('{} {}'.format(name, age))
        parts = input().split()
        name = parts[0]