# #練習：定義一個計算質數的函數。

# ❏ Requirements：

# 1. 讓使用者輸入一個整數 n

# 2. 請分別定義兩個 Function: isPrime(n) 回傳 n 是否為質數、primes(n) 回傳小於 n 質數

# ❏ Sample Input： 20 ← 使用者輸入

# ❏ Sample Output： 2, 3, 5, 7, 11, 13, 17, 19 ← 畫面輸出

# ❏ Sample Code：

# Sieve of Eratosthenes

def isPrime(x):
    if x <2 : return False
    for i in range(2, int(x**0.5) +1):
        if x % i == 0:
            return False
        else:
            return True

def Prime(x):
    if x < 2:  # 沒有小於2的質數
        return []
    prime = [1] * (x + 1)  # 質數列表初始化，範圍擴展到x+1
    prime[0], prime[1] = 0, 0  # 0和1不是質數，設為0
    
    for i in range(2, int(x**0.5) + 1):  # 只需檢查到x的平方根
        if prime[i]:  # 如果i是質數
            for j in range(i * 2, x + 1, i):  # 從i的兩倍開始，標記所有i的倍數為非質數
                prime[j] = 0

    # 從列表中獲取所有質數的索引
    primes = [i for i, is_prime in enumerate(prime) if is_prime]
    return primes

# 用戶輸入並呼叫函數
x = int(input("請輸入一個數字："))  # 確保輸入轉為整數
print(isPrime(x))
print(Prime(x))


# ex: x = 20
# 那麼 我的設定會把他們另成 [1,1,1,1,1,1,1,...]

# prime[0] == prime[1] 0跟1 不會是質數 所以 => [0,0,1,1,1,...]

# 從2開始 逐步排除2 的倍數 3的倍數 5的倍數 如果是的話在prime標記為0

# 使用 i, if is_prime in enumerate(prime) 如果是1 就把那 i print 出來