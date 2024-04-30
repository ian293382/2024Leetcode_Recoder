
S = 'Here are UPPERCASE and lowercase chars.'

count_words ={}
for i , char in enumerate(S):
    count_words.setdefault(char, [])
    # {'H': [], 'e': [], 'r': [], ' ': [], 'a': [], 'U': [], 'P': [], 'E': [], 'R': [], 'C': [], 'A': [], 'S': [], 'n': [], 'd': [], 'l': [], 'o': [], 'w': [], 'c': [], 's': [], 'h': [], '.': []}
    count_words[char].append(i + 1)

print(count_words)
# Task #04 作業 01【參考解答】字串的位置分佈