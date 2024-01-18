from typing import List

# 1. 什么样的时候容积最大呢？底最大，两边的高最大，此时容积是最大的
# 2. 怎样找到最大呢，尽可能少的移动，两边的高都尽可能大
# 3. l r 两个指针移动，max记录容积，两个指针移动，由小的进行移动，一直移动到小的时候，然后确定容积
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_num=0
        while l<r :
            min_num=min(height[l],height[r]) #找到最小的
            max_num=max(max_num,min_num*(r-l)) # 求最大的容积
            # 此时需要移动小的那个前进，找到比当前下标大的
            while l<r and height[r]<=min_num:
                r-=1
            while l<r and height[l]<=min_num:
                l+=1
        return max_num