
def twoSum(nums, target):
    ans_dict =  {}
    for i , num in enumerate(nums):
        num2 = target - num
        if num2 in ans_dict:
            return [ans_dict[num2], i]
        ans_dict[num] = i  
twoSum(nums =[2,7,11,15], target = 9)
# Task #03 作業 02【參考解答】Two Sum