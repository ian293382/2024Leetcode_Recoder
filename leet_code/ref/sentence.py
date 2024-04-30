# ❏ Requirements：

# 1. 讓使用可以輸入一個字串 S

# 2. 去計算字串中每個字母所出現的位置並且存入一個 list

# 3. 將出現字母當作 key、出現位置所組成的 list 組裝成一個 dict 後印出

# ❏ Sample Input #01：Here are UPPERCASE and lowercase chars. ← 使用者輸入

# ❏ Sample Output #01：{'H': [1], 'n': [21], 'o': [25], 'U': [10], 'r': [3, 7, 28, 37], 'l': [24], 's': [31, 38], 'c': [29, 34], 'e': [2, 4, 8, 27, 32], 'S': [17], ' ': [5, 9, 19, 23, 33], 'a': [6, 20, 30, 36], 'R': [14], 'w': [26], '.': [39], 'h': [35], 'E': [13, 18], 'd': [22], 'P': [11, 12], 'A': [16], 'C': [15]} ← 畫面輸出

# ❏ Sample Code：

S = 'Here are UPPERCASE and lowercase chars.'

ans_dict = {}
for i, s in enumerate(S):
  ans_dict.setdefault(s, [])
  ans_dict[s].append(i + 1)


print(ans_dict) # {'H': [1], 'n': [21], 'o': [25], 'U': [10], 'r': [3, 7, 28, 37], 'l': [24], 's': [31, 38], 'c': [29, 34], 'e': [2, 4, 8, 27, 32], 'S': [17], ' ': [5, 9, 19, 23, 33], 'a': [6, 20, 30, 36], 'R': [14], 'w': [26], '.': [39], 'h': [35], 'E': [13, 18], 'd': [22], 'P': [11, 12], 'A': [16], 'C': [15]} 


# S = 'Here are UPPERCASE and lowercase chars.'

# d = {}
# count = 1
# for s in S:
#   if s not in d:
#     d[s] = []
#   d[s].append(count)
#   count = count + 1

# print(d)