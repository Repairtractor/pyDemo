# 这道题首先就想到滑动窗口
# 滑动窗口，首先确定循环不变量，
# i...j 表示无重复的最长子串， existSet记录存在的字符，max是最大的长度， j一直移动，max++，直到existSet中有重复的数据，此时exist删除，i++，num--
# 一直到遍历整个数据
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        exist=set()
        i=j=0
        max_num=num=0
        while j<len(s):
            while s[j] in exist:
                max_num=max(max_num,num)
                exist.discard(s[i])
                i+=1
                num-=1
            exist.add(s[j])
            j+=1
            num+=1
            max_num=max(max_num,num)
        return max_num

            
                

