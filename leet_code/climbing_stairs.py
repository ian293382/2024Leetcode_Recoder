#練習：You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# ❏ Requirements：

# 1. 讓使用者輸入一個數字 n ，代表需要爬到的階層數量

# 2. 每次可以往上移動一階或兩階，計算爬到 n 階有幾種可能的走法

# ❏ Sample Input #1: 2 ← 使用者輸入

# ❏ Sample Output #1: 2 ← 畫面輸出（說明：爬到 2 階可能是 1 + 1 or 2）

# ❏ Sample Input #2: 3 ← 使用者輸入

# ❏ Sample Output #2: 3 ← 畫面輸出（說明：爬到 3 階可能是 1 + 1 + 1 or 1 + 2 or 2 + 1）

# ❏ Sample Code：

n = input()  

def climbStairs(n: int) -> int:
    #     if n == 1:
    #     return 1
    # if n == 2:
    #     return 2

    # # 创建一个列表来存储到达每个台阶的方法数
    # dp = [0] * (n + 1)
    # dp[1] = 1  # 到达第1阶有1种方法
    # dp[2] = 2  # 到达第2阶有2种方法

    # # 从第3阶开始计算到达每一阶的方法数
    # for i in range(3, n + 1):
    #     dp[i] = dp[i - 1] + dp[i - 2]

    # return dp[n]
    W = [0,1,2]
    if len(W) < n+1:
        return climbStairs(n - 2) + climbStairs(n - 1)
    return W[n]

print(climbStairs(n)) 


# 完成後也請你繳交程式碼的同時，也複製以下格式填上關於這個練習的實作回顧：

# ---

# 1️⃣ 這個題目對你來說難易度為何？＿＿＿＿＿＿＿

# 2️⃣ 撰寫過程中，你有學習到什麼新的用法？＿＿＿＿＿＿＿

# 3️⃣ 請嘗試幾種不同的優化的方法？＿＿＿＿＿＿＿