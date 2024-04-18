Task #09 作業 01【簡答題】函式使用
繳交作業時請直接複製以下題目到作業填答區，並將「(在這裡回答)」部分改寫成你的答案，不用附上題目、標題設定成「2024 Task#09 作業 01」：

1. 解釋看看你心中的「函式」是什麼？為什麼要使用「函式」？

函式是可以將程序進行整理 管理 維護 擴展功用

2. 試著說明以下程式的「執行順序」，執行的順序會長怎樣（盡可能地拆分為運算的最小單位）？

def f(a, b):
    if a > b:
        return a
    return b
>>> import dis    
>>> dis.dis(f)
  <!-- 1           0 RESUME                   0

  2           2 LOAD_FAST                0 (a)
              4 LOAD_FAST                1 (b)
              6 COMPARE_OP               4 (>)
             12 POP_JUMP_FORWARD_IF_FALSE     2 (to 18)

  3          14 LOAD_FAST                0 (a)
             16 RETURN_VALUE

  4     >>   18 LOAD_FAST                1 (b)
             20 RETURN_VALUE -->

這個函式運作方式從 a 變量載入 ， 再從b 參數載入 經過比較運算(COMPARE_OP) 如果是的話 把a的值 傳出  不是的話傳出 b 

max = f(3, 5)
a = 3 b = 5 傳入函式
max = f(6, f(3, 5))
a = 6 b = f(3, 5) b 先處理完 b=5 在帶入 f True = a =  6
max = f(max, f(1, 2)) 
當前max =  6  同上面理論 b = 2 最後反傳max = 6

3. 以下程式可以會傳 a, b 的最大值，如何改寫成可以接收 f(a, b), f(a, b, c), f(a, b, c, ...) 等不同個數輸入的最大值函式可以怎麼做？

def f(a, b):
    if a > b:
        return a
    return b

f(3, 5) # O
f(3, 4, 5) # X
f(3, 4, 5, 6, 7) # X

# 可以使用可邊參數*arg 

def f(*args):
    if not args:
        return None
    max_value = args[0]
    for num in args:
        if num > max_value:
            max_value = num
    return max_value

    

4. 請問下方程式碼會回傳什麼結果？

a = 'A'

def f(b):
    a = 'AAA'
    c = 'C'
    print(a)
    print(b)
    print(c)
    return b

print(a)
print(f('B'))
print(a)
(在這裡回答)

5. 請問下方程式碼會回傳什麼結果？

a = 'A'

def f(b):
    c = 'C'
    print(a)
    a = 'AAA'
    print(b)
    print(c)
    return b

print(a)
print(f('B'))
print(a)
(在這裡回答)