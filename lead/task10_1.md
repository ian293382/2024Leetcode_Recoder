Task #10 作業 01【簡答題】例外處理
繳交作業時請直接複製以下題目到作業填答區，並將「(在這裡回答)」部分改寫成你的答案，不用附上題目、標題設定成「2024 Task#10 作業 01」：

1. 回想看看到目前為止，你曾經遇到過哪些錯誤發生？

沒特別記得

2. 試著解釋什麼是「例外處理」，並且說明在哪些情況適合使用？

可能逾時會用到 或購物車的假購買會用到

3. 請問以下程式碼的「變數 e」代表的意義是什麼？

try:
    x = input() / input()
except Exception as e:
    print(e)
Exception 為異常的基本 e 的變數 將這個錯誤存放在Exception裏面

4. 請問以下程式碼的「raise」跟「finally」的用法為何？

try:
    raise Exception('spam', 'eggs')
except Exception as e:
    print(e)
finally:
    print('done')


當他嘗試補貨到有'spam' 或'eddgs'時 會pring出他們自己最後會用'done'清除異常 讓程序繼續運行