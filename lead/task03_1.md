1. 請問字串型態中「'...'」跟「"..."」中單、雙引號有什麼差別，使用上該如何選擇？

單引號跟雙引號沒有什麼分別 但要注意不能混用

2. 在 Python 使用 s[3:8] 會取出 s 字串中的哪些字串？該怎麼解釋這個語法？

他會取出s 字串的第4 到 7 個字串 

3. 在 Python 使用 s[::-1] 會取出 s 字串中的哪些字串？該怎麼解釋這個語法？

這個會使s字串進行反轉

4. 在 Python 使用 s[0:len(s):-1] 會取出 s 字串中的哪些字串？該怎麼解釋這個語法？

空字串  他是從0開始到len(s) 整個字串的輸入但是 每一步從 -1 方向前進所以 呈現空字串 

5. 請問 Python 中的字串型態是 mutable 還是 immutable？該怎麼判斷呢？

immutable 他的值永遠固定 不能做更改 
>>> s = "hello"
>>> s[1] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment