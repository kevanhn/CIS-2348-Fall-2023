# Kevin Nguyen 1928145

def selection_sort_descend_trace(num):
    for i in range(len(num) - 1):
        x = i
        for j in range(i + 1, len(num)):
            if num[x] < num[j]:
                x = j
        num[i], num[x] = num[x], num[i]
        for value in num:
            print(value, end=" ")
        print()
    return num


if __name__ == "__main__":
    num = []

    num = [int(x) for x in input("").split()]
    selection_sort_descend_trace(num)
