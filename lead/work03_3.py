
# #練習：試著用 Python 將網址當中的 domain 取出來。

# ❏ Requirements：

# 1. 讓使用者可以輸入一個網址

# 2. 利用程式取出網址當中的 domain 後輸出

# ❏ Sample Input： https://www.facebook.com/dscareer ← 使用者輸入

# ❏ Sample Output： www.facebook.com ← 畫面輸出

# ❏ Sample Code：
# Hint：可以利用 dir(str) 找到 split，再利用 help(str.split) 查詢怎麼使用
s = input() # https://www.facebook.com/dscareer

# [0]是被切出去的東西 ex s.split('//')[0] = ['https:', 'www.facebook.com/dscareer']
ans = s.split('https://')[1].split('/')[0]

print(ans) # www.facebook.com
