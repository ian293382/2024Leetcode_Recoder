# #練習：Self-Dividing Number（自除數）指的是可以被每位數的數字整除的數，例如，128 可以同時被 1、2、8 分別整除即符合。本題請根據輸入的上下邊界，找出該區間內的 Self-Dividing Number 中哪兩個數之間的差距最大。舉個例子，假如從 11 - 20 符合的數有：11、12、15，其中 11 跟 12 的差距等於 1、12 跟 15 的差距等於 3，因此差距最大是 12 跟 15。

# ❏ Requirements：

# 1. 讓使用者輸入兩個數字，代表一個區間

# 2. 請利用程式找出該區間中符合 Self-Dividing Number 的所有數

# 3. 將差距最大的 Self-Dividing Number 相鄰兩數印出

# ❏ Sample Input #1: 11, 20 ← 使用者輸入

# ❏ Sample Output #1: (12, 15) ← 畫面輸出

# ❏ Sample Input #2: 100, 900 ← 使用者輸入

# ❏ Sample Output #2: (555, 612) ← 畫面輸出

# ❏ Sample Code:
# Task #03 作業 01【參考解答】Self-Dividing Number 目前寫不出來

def is_self_dividing(n):
    """檢查一個數字是否是自除數"""
    str_n = str(n)
    for char in str_n:
        if char == '0' or n % int(char) != 0:
            return False
    return True

def max_self_diving_difference(a, b):
    """找出範圍 [a, b] 內所有自除數之間的最大差距"""
    dividing_list = []
    for i in range(a, b + 1):
        if is_self_dividing(i):
            dividing_list.append(i)
    
    if not dividing_list or len(dividing_list) < 2:
        return None  # 如果沒有自除數或不足兩個，則返回 None

    max_diff = 0
    max_diff_pair = None

    for i in range(len(dividing_list) - 1):
        current_diff = dividing_list[i + 1] - dividing_list[i]
        if current_diff > max_diff:
            max_diff = current_diff
            max_diff_pair = (dividing_list[i], dividing_list[i + 1])

    return max_diff_pair

# 輸入處理
a = int(input("請輸入範圍的起始值: "))
b = int(input("請輸入範圍的終止值: "))

# 計算並輸出結果
max_diff_pair = max_self_diving_difference(a, b)
if max_diff_pair:
    print(f"最大差距的 Self-dividing Numbers 是 {max_diff_pair[0]} 與 {max_diff_pair[1]}，差距為 {max_diff_pair[1] - max_diff_pair[0]}")
else:
    print("範圍內沒有足夠的自除數來計算最大差距。")