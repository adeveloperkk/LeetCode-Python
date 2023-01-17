#credit(https://github.com/adeveloperkk/LeetCode-Python)
#17jan'2023
class Solution(object):
    def twoSum(self,nums, target):
        dic={}
        for i in range(len(nums)):
            if target-nums[i] in dic:
                return [dic[target - nums[i]],i]
            else:
                dic[nums[i]]=i
                
                
