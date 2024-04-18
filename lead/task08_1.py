# #練習：階乘總和

# ❏ Requirements：

# 1. 利用迴圈讓使用者可以重複輸入一個數字 n

# 2. 利用程式計算 1! + 2! + 3! + ... + n! 的總和

# 3. 每一個回合請將階乘總和的結果印出

# ❏ Sample Input： 4 ← 使用者輸入

# ❏ Sample Output： 33 ← 畫面輸出

# ❏ Sample Code：

x = input() # 4
f = 1
if x.isdigit():
    x = int(x)
    f = 1 
    # sum([1,2,3])
    level_sum = sum(list(f := f * i for i in range(1, x + 1)))
    print(level_sum) 
    
# for num in range(1, x+1):
#   f1 *= num
#   f += f1
# print(f)