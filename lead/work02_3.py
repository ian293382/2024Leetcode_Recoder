# ❏ Requirements：

# 1. 輸入兩個正整數存入變數 a, b

# 2. 請輸出 a, b 變數內容交換後的結果（不是輸出順序交換而已）

# 3. 程式當中不可以使用 if 或 loop

# ❏ Sample Input： 5 10 ← 使用者輸入

# ❏ Sample Output： 10 5 ← 畫面輸出

# ❏ Sample Code：

a = input() 
b = input()
print(a, b) # 5, 10

# ans_set = (a,b)

# a = ans_set[1]
# b = ans_set[0]

a, b = b , a 
print(a, b) # 10, 5