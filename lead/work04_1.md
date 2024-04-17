
1. 請問 List 是 Python 中常見的容器型態，他跟一般的 int、float 這類型態有什麼不同嗎？

 int、float  只能存放一筆資料 也就是單元型態(Primary), List 為容器型態 可以在一個變數內存放一組資料
 List、Tuple、Dictionary、Set 為容器型態資料格式。

2. 試著解釋 list 底下的 append 用法是什麼？

（Hint: 可以利用 dir(list) 找到 append，再利用 help(list.append) 查詢怎麼使用）


append(self, object, /)
    Append object to the end of the list.
  => 可以在 list 再添加新的append的物件



3. 請問 list 當中的 append(...) 跟 extend(...) 有什麼不一樣的地方？

extend(self, iterable, /)
    Extend list by appending elements from the iterable.
    
    Extend是可以將 一組資料疊加在原本List 資料上

4. 請問 list 當中的 reverse(...) 跟 [::-1] 有什麼一樣和不一樣的地方？

>>> b = [1, 2, 3, 4]  
>>> c = b[::-1]
>>> c
[4, 3, 2, 1]
 
>>> a = b.reverse()
>>> a
=> reverse() 的值不會進行新建資料的動作而是在原本的列表資料進行反轉 會return None 沒有回傳值 
=> [::-1] 為切片操作，會進資料新增的動作會反傳一個新的列表

5. 請問如果直接用以下方法複製 List，可能會存在什麼疑慮嗎？

a = [1, 2, 3, 4, 5] 
b = a

第一句話是將 [1, 2, 3, 4, 5] 指派給 a 也就是  a的物件指向為 [1, 2, 3, 4, 5]
第二句話是 a 指派給 b  也就是 b的物件指向為 a 只是a 恰巧存入了 [1, 2, 3, 4, 5]

他們雖然存取相同資料但是 是不同物件 不能將a 物件代替 b 物件去使用 
