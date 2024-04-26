# 确定一个数是不是回文数，bab就是一个回文数
# 解：如果用头尾两个指针，判断是否相等，l>r时说明比较完毕  例如 bab  当l为2 r为1时比较结束。
class Solution:
    # 解1
    def isPalindrome(self, x: int) -> bool:
        #1. 转成字符串
        str_x=str(x)
        l=0
        r=len(str_x)-1
        #2. 设置l，r两个变量从字符串的左右两边进行比较，不想等时结束  
        while(l<=r):
            if str_x[l]!=str_x[r]:
                return False
            l+=1
            r-=1
        return True
   # 解2：解1是转成字符串的处理方式，还有一种是直接用整数处理，但是这里就涉及到了一个溢出的情况，要谨慎处理
    def isPalindrome1(self, x: int) -> bool:
        res=0
        curr=x
        while curr>0:
            res=res*10+curr%10
            curr//=10
    
        return True if res==x else False
    
    # 解3：题解2的优化版本，其实只需要比较一般就好了，一半的时候值相当，那么就是回文数
    def isPalindrome2(self, x: int) -> bool:
        res=0
        curr=x
        while curr>0:
            res=res*10+curr%10
            curr//=10
            if res==curr or curr//10==res:
                return True
        return False
            
    
cc=Solution().isPalindrome2(121)
print(cc)