# 学习python的第一条注释，求双数之和，暴力解题

from typing import List #List需要导包

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for index in range(len(nums)):
            if target-nums[index] in d:
                return index,d.get(target-nums[index])
            d[nums[index]]=index

        

cc=Solution().twoSum1([1,2,3,4],3)
print(cc)

        