
#練習：元素位置異動

# ❏ Requirements：

# 1. 建立一個列表（List ）初始化為 1, 2... 9 的元素

# 2. 利用程式將最左邊的元素移動到最右邊

# 2. 最後請將移動的結果印出

# ❏ Sample Input： [1, 2, 3, 4, 5, 6, 7, 8, 9] ← 預設初始化

# ❏ Sample Output： [2, 3, 4, 5, 6, 7, 8, 9, 1] ← 畫面輸出

# ❏ Sample Code：

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

s =  L[1:10] + [L[0]]

print(s) # [2, 3, 4, 5, 6, 7, 8, 9, 1]

# s = L[1:9]
# s.append(L.pop(0))


1️⃣ Github Repo 網址：https://github.com/ian293382/colab_mask_data/blob/main/project_data.ipynb

2️⃣ 今天的練習難易度可以如何？ 第三段有點卡住

3️⃣ 過程中有遇到什麼問題或是心得嗎？＿＿＿＿＿＿＿

4️⃣ 上傳一張執行結果的截圖：＿＿＿＿＿＿＿