# #練習：奇偶數分堆

# ❏ Requirements：

# 1. 建立一個列表（List ）初始化為 0, 1, 2... 9 的元素

# 2. 請利用條件判斷與迴圈將 List 中的奇數放在前面、偶數放在後面

# 3. 最後請將分堆後的結果印出

# ❏ Sample Input： [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] ← 預設初始化

# ❏ Sample Output： [1, 3, 5, 7, 9, 0, 2, 4, 6, 8] ← 畫面輸出

# ❏ Sample Code：

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd = []
even = []
for i in L:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
    L = odd + even
print(L)
# [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]