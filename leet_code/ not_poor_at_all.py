# ❏ Requirements：

# 1. 讓使用者輸入一個字串 s

# 2. 利用程式將字串中出現的 not … at all 取代成 good 後輸出（Note: 可以假設字串中最多只會出現一次 not ... at all）

# ❏ Sample Input #1: This company is not poor at all. ← 使用者輸入

# ❏ Sample Output #1: This company is good. ← 畫面輸出

# ❏ Sample Input #2: I'm not at all happy about it. ← 使用者輸入

# ❏ Sample Output #2: I'm good happy about it. ← 畫面輸出

# ❏ Sample Code:

s = input() # This company is not poor at all``. 


# 目前程度切片
if 'at all' in s:
    split_front = s.split('not')
    # ['a is ', ' poor at all banana'] 前面去掉
    split_back = split_front[1].split('at all')
    # ['a is ', ' poor at all banana'] 後面去掉
    ans_sentence = split_front[0] + 'good' + split_back[1]


print(ans_sentence) # This company is good.


# Task #02 作業 01【實作題】複雜的字串取代 - 參考解答
# import re

# s = input()  

# # 使用 re.sub 函式來進行正規表達式取代
# d = re.sub(r"not\s+.*?\s+at\s+all", "good", s)  
# d = re.sub(r"not\s+.*?\s+at\s+all", "good", s)
# print(d)  