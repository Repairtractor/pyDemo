from typing import List


class Solution:
    # 找到最大的公共前缀，那么暴力一点每次拿出第一个的[0...l]字符去比较所有的字符串的前缀，有一个不对，那就返回[0...l-1]的字符串
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs==False:
            return ""
        if len(strs) == 1:
            return strs[0]
        first_str = strs[0]
        for index in range(len(first_str)):
            x = first_str[index]
            for item in strs:
                if index>=len(item) or x!=item[index]:
                    return  first_str[0:index] if index>0 else ""
        return first_str
    
    # 另一种解法是先排序，然后比较头部和尾部
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        if strs==False:
            return ""
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        head=strs[0]
        tail=strs[len(strs)-1]
        for index in range(len(head)):
            if index>=len(tail) or tail[index]!=head[index]:
                return head[0:index] if index>0 else ""
        return head



strs = ["ab", "a"]
cc=Solution().longestCommonPrefix(strs)
print(cc)
