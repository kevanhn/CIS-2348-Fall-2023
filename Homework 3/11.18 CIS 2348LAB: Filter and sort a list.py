# Kevin Nguyen 1928145

input_str = input()
integers = [int(x) for x in input_str.split()]

non_negative_integers = [x for x in integers if x >= 0]
non_negative_integers.sort()

for num in non_negative_integers:
    print(num, end=' ')
