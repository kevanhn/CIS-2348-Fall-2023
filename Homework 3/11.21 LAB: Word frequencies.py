# Kevin Nguyen 1928145

input_str = input()

words = input_str.split()

word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

for word in words:
    print(f"{word} {word_freq[word]}")
