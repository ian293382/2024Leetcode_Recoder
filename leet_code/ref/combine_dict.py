#練習：在 Python3.9+ 版本的有一種新的字典運算「|」，
# 可以用來將多個字典內的元素合併。那想請問你的是
# ，在 Python3.9 版本以前，我們可以怎麼將多個字典合併成一個新的字典呢？

# ❏ Requirements：

# 1. 利用程式將多個字典內的元素合併成一個新的字典

# 2. 合併過程中請勿直接使用「|」運算

# ❏ Sample Input #1: {1:10, 2:20}、{3:30, 4:40}、{5:50, 6:60} ← 預設初始化

# ❏ Sample Output #1: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 6
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

ans_dict = {}
ans_dict.update(dic1)
ans_dict.update(dic2)
ans_dict.update(dic3)


print(ans_dict) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Task #02 作業 03【實作題】字典元素合併 - 參考解答
# d = {**dic1.**dic2, **dic3}

# d = {}
# for i in range(1, 4):
#     d.update(globals()[f"dic{i}"])
# print(d)

d = {}
for i in range(1,4):
    d.update(globals()[f"dic{i}"])
print(d)

# python 3.9

#  a = dic1| dic2 | dic3