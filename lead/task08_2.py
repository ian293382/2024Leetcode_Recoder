#練習：字母頻率（frequency of letters; character frequencies），
# 指的是各個字母在文本材料中出現的頻率。常被應用於密碼學，尤其是可破解古典密碼的頻率分析。
# 例如，摩斯密碼中越常用的字母，其編碼符號就越短；而數據壓縮技術中也有相似的方法，
# 如夫曼編碼就是按來源符號出現的機率大小去編碼。接下來，讓我們來試試看如何在 Python 實現從字串中計算每個字母出現頻率的問題？

# ❏ Requirements：

# 1. 讓使用者可重複輸入字串

# 2. 每一回合計算該字串中每個字母的出現次數並且存入 dict 中

# 3. 將使用者輸入字串的字母及其計數印出

# ❏ Sample Input： Hello World ← 使用者輸入

# ❏ Sample Output： {‘H’: 1, ‘e’: 1, ‘l’: 3, ‘o’: 2, ‘ ’:1, ‘W’: 1, ‘r’: 1, ‘d’: 1} ← 畫面輸出

# ❏ Sample Code：

x = input() # Hello World

# for i in x:
#    print(i , x.count(i))
#  目前自己解 fail

# word_dict = {}
# for word in x:
#     if x in word_dict:
#         word_dict[word] += 1
#     else:
#         word_dict[word] = 1

word_dict = {i: x.count(i) for i in x}

print(word_dict) # {‘H’: 1, ‘e’: 1, ‘l’: 3, ‘o’: 2, ‘ ’:1, ‘W’: 1, ‘r’: 1, ‘d’: 1}