. 請簡單描述程式中必備的三種結構，以及他們的運作流程為何？

(在這裡回答)

2. 請問以下描述會回傳什麼結果？

x = 6
y = 5
z = 7

print((x > y )and (y > z) or (y - z % 2 > x) or (z + x*6 > y**2))
  True and False => False 
  False or False => False
  False or True => True 
>>> True

3. 請問下方程式碼會回傳什麼結果？

a = 10
while a:
    a = a - 1
    print(a)
9
8
7
6
5
4
3
2
1
0 

4. 請問下方程式碼會回傳什麼結果？

a = list(range(6))
while a:
    a.pop()
    print(len(a))

a.pop() => 去掉做後一個數字 

5
5
4
4
3
3
2
2
1
1
0
0
