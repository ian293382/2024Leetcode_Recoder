1. 請比較 Python 中的四種容器彼此間差別是什麼？
    四種容器型態 (container) =  List , set , dictionary ,tuple
    1. 有序容器=> tuple, list 但是tuple 是不可變的 將值做更改 會變成 TypeError 異常。
    2. 無序容器=> dictionary, set 是無序的 可變量 但是set 出來的值通常是唯一的 用來消除list 重複的list。
    3. Dictionary 的key 值是唯一的。
    4. 要記住使用 my_tuple = (1,)

2. 請解釋 Tuple 的「immutable」是什麼意思？

immutable = 裡面存放的資料不能更改
myTuple = (1 ,2 , 3)
# 會拋出TypeError  
my_tuple[0] = 4  => 要改變的話建議使用list

3. 當存取字典中不存在的 Key，會發生什麼事？該如何解決？

d = {1: 'a'}
print(d[2])

=> 會發生KeyError:2  使用 get() 可以避免字典中的值
=> print(d.get(2, 'key  not found')) 
如果有值 
=> print(d.get(1, 'key  not found')) =  a
   

4. 請問在 Python 中的 Dictionary 是否支援「+」運算？請解釋你的原因？

因為 dictionary 每一個key值 為唯一 如果 + 產生則還要去做判別 key 值 是否重複

5. Python 的集合是不允許存放列表的，你可以想想看為什麼嗎？

=> set 具有唯一性 和不可變性 如果使用list  去做操作可能會導致 重複值的出現
