#練習：map(…) function 是 Python 中常用的一種 functional method，可以對列表內的所有元素進行同一個 function 操作。 接下來，請你試試看在 Python 中實現一個自定義的 map(F, L) 方法。

# ❏ Requirements：

# 1. 請先完成 add1 和 isPrime 兩個函式（add1(n) 會回傳 n+1、isPrime(n) 會判斷 n 是否為質數）

# 2. 利用程式實作 map 函式，map(F, L) 包含兩個參數輸入，F 是一個 function、L 是一個列表，回傳結果是一個列表

# 3. 本提要求自己實作 map(...) 函式，請勿直接使用內建的 map(…)

# ❏ Sample Input #1: L = [1,2,3,4,5,6], F = add1(n) ← 預設初始化

# ❏ Sample Output #1: [2,3,4,5,6,7] ← 畫面輸出

# ❏ Sample Input #2: L = [2,3,4,5,6,7], F = isPrime(n) ← 預設初始化

# ❏ Sample Output #2: [True,True,False,True,False,True] ← 畫面輸出

# ❏ Sample Code:

def add1(n):
  return n+1

def isPrime(n):
    return all( n %d for d in range(2, int(n** 0.5)+1))


def f(L, F):
    return [F(item) for item in L]

L = [1,2,3,4,5,6]
F = add1
print(f(L, F)) # [2,3,4,5,6,7]

L = [2,3,4,5,6,7] 
F = isPrime
print(f(L, F)) # [True,True,False,True,False,True]