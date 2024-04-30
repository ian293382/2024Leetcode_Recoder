#練習：請根據使用者的輸入的字串，產生不重複的排列組合。

# ❏ Requirements：

# 1. 讓使用者重複輸入字串，取出字串中出現過哪些字母

# 2. 計算由這些字母所組成的所有排列組合存入列表

# 3. 每回合將列表內的字串依照字母排序後印出

# ❏ Sample Input #1: A ← 使用者輸入

# ❏ Sample Output #1: A ← 畫面輸出

# ❏ Sample Input #2: AB ← 預設初始化

# ❏ Sample Output #2: AB, BA ← 畫面輸出

# ❏ Sample Code： Task #05 作業 01【參考解答】不重複的排列組合

# s = input() # AB

# d = []
# def permute(s, i, length):
#     if i == length:
#         d.append("".join(s))
#     else:
#         for j in range(i, length):
#             s[i], s[j] = s[j], s[i]
#             permute(s, i+1, length)
#             s[j], s[i] = s[i], s[j]

# permute(list(s), 0, len(s))
# print(d)
# # ['AB', 'BA']

from itertools import permutations

s= input()

d = [''.join(i) for i in permutations(s)]
print(d)