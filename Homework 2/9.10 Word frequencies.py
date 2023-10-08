# Kevin Nguyen 1928145
import csv

def main():
    input_filename = input()

    file = open(input_filename)

    word_counts = csv.reader(file, delimiter=',')

    words = []

    for row in word_counts:
        for word in row:
            words.append(word.strip())

    for i in range(len(words)):
        if words[i] not in words[:i]:
            count = 0
            for w in words:
                if words[i] == w:
                    count += 1
            print(words[i], count)
    file.close()

if __name__ == "__main__":
    main()
