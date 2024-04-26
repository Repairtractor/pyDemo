#给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
#如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。


# 解：将这个整数每次%10得到最后一位的数字，然后再/10设掉最后一位，新的数字每次*10 +下一位数字，最后反转的数字如果绝对值大于2^31 返回0

class Solution:
    def reverse(self, x: int) -> int:
       curr=abs(x)
       result=0

       while curr>0:
            result=(result*10)+curr%10
            curr//=10
       if not is_in_32bit_signed_range(result if x>0 else -result):
           return 0
       return result if x>0 else -result
    # 题解2，假设不能用超过32位的数字存储呢？可以在最后一次时判断是否大于 2**31%10,大于就不用比较了，那么这个数必然溢出，小于必然不溢出
    # 等于时继续判断最后一位数字是否大于7/8，如果大于说明也会溢出
    def reverse2(self, x: int) -> int:
        # 首先找到32位的边界，这里最好不要去记忆，而是直接进行运算求
        max=2**31//10
        last_max=2**31%10

        curr=abs(x)
        res=0
        while curr>0:
            temp=curr%10
            if res>max or (res==max and temp>(last_max if x<0 else last_max-1)):
                return 0
            res=res*10+temp
            curr//=10
        return res if x>0 else -res
    
def is_in_32bit_signed_range(x):
    return -2**31 <= x <= 2**31 - 1

cc=Solution().reverse2(1463847412)
print(cc)





