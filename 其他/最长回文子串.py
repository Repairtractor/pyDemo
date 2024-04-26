# 先暴力解法试一下，双循环，依次遍历 abcb，找到最大的max_len
# 我们用一个 boolean dp[l][r] 表示字符串从 i 到 j 这段是否为回文。试想如果 dp[l][r]=true，我们要判断 dp[l-1][r+1] 是否为回文。只需要判断字符串在(l-1)和（r+1)两个位置是否为相同的字符，是不是减少了很多重复计算。
# 进入正题，动态规划关键是找到初始状态和状态转移方程。
# 初始状态，l=r 时，此时 dp[l][r]=true。
# 状态转移方程，dp[l][r]=true 并且(l-1)和（r+1)两个位置为相同的字符，此时 dp[l-1][r+1]=true。
class Solution:
    def longestPalindrome1(self, s: str) -> str:
        max_len=bigin=end=0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if self.compara(s,i,j) and j-i+1>max_len:
                    max_len=(j-i+1)
                    bigin=i
                    end=j
        return s[bigin:end+1]

    def compara(s:str,i:int,j:int)->bool:
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
    
    # 试一下中心扩散法
    # 中心扩散法就是以一个位置为中心往左右扩散，寻找不等于中心点的数据，
    # 找到不等于中心点的数之后，比较左右的点是否相同，如果相同就认为是一个回文子串，记录串的长度，每次begin和end记录大的起始下标，最后返回
    def longestPalindrome(self, s: str) -> str:
        begin=end=max_len=0 # 子串起始位置，以及最大长度
        for i in range(0,len(s)):
            l=r=i
            # 往左边寻找
            while l>=0 and s[l]==s[i]:
                l-=1
            while r<len(s) and s[i]==s[r]:
                r+=1
            # 两边相等的数据也都是回文子串
            while l>0 and r< len(s) and s[l]==s[r]:
                l-=1
                r+=1
            # 此时已经找到匹配的回文子串，但是可能并不是最大的
            if max_len<(r-l):
                max_len=(r-l)
                begin=l
                end=r
        return s[begin:end+1]

print(Solution().longestPalindrome('abcb'))

                
                









        


        

