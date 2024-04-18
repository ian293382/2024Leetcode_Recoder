# 2. 利用程式計算 n! 的結果並且印在畫面上

# ❏ Sample Input #01： 4 ← 使用者輸入

# ❏ Sample Output #01： 24 ← 畫面輸出

# ❏ Sample Input #02： a ← 使用者輸入

# ❏ Sample Output #02： a 是一個不合法的輸入，無法運算 ← 畫面輸出

# ❏ Sample Code：

x = input() # 4
# 轉成INT 不然會衛報錯誤
if x.isdigit():
    x = int(x)
    f = 1  
    for i in range(1, x + 1):
        f *= i
    print(f"f階乘結果為: {f}")
else:
    print(f"{x} 不是數字，無法運算")