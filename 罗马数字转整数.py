# 罗马数字转整数,大值的左边都是减少，右边时增加
# 从左边开始移动，移动的数值都是加法，找出最大值，当找到比当前值还大时，现有的数据变成减，
# 就是看两位被，后一个比前一个大，说明就是后一个减前一个，然后加上值，相同就直接加
class Solution:
    def romanToInt(self, s: str) -> int:
        curr=res=0
        next=1
        # 遍历curr，只需要判断下一个数据是否大于当前的数，如果大于就减，小于就加
        while curr<len(s):
            


        



        return 0
    
    def mapping(self,s:str)->int:
        return {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }.get(s,'default')