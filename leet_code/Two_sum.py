#練習：Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

# ❏ Requirements：

# 1. 預設題目會提供兩個變數 nums 列表和 target 整數

# 2. 請找出 nums 中兩數和為 target 值的 index 並存放在列表後印出

# ❏ Sample Input #1: nums = [2,7,11,15], target = 9 ← 預設初始化

# ❏ Sample Output #1: [0,1] ← 畫面輸出

# ❏ Sample Input #2: nums = [3,2,4], target = 6 ← 預設初始化

# ❏ Sample Output #2: [1,2] ← 畫面輸出

# ❏ Sample Code:

nums =[2,7,11,15], target = 9
def twoSum(nums, target):
 # 創建一個字典用於存儲已經遍歷過的數字和它們的 index
    visited = {}
    # 遍歷整個列表
    for i, num in enumerate(nums):
        # 計算與目標值的差值
        num2 = target - num
        # 如果差值已經存在於 visited 中，返回差值的 index 和當前的 index
        if num2 in visited:
            return [visited[num2], i]
        # 將當前數字和 index 存入 visited 中
        visited[num] = i
    # 如果找不到符合條件的組合，返回空列表
    return []