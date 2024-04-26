from typing import List

# 寻找中位数
# 两个指针i,j 一个数组，假设mid=（m+n)/2 如果（m+n)%2=0 那么中位数=(（mid-1)+(mid))/2.0
# 如果（m+n)%2!=0 那么中位数=mid
# 中位数意味着左边一半，右边一半，所以只需要设定好奇数和偶数时要排序的数组大小，然后当排序到此时直接返回，后面直接计算中位数就好
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        if m==0 and n==0:
            return 0
        i=j=0
        num=[]
        max_num= (m+n)//2+1
        while i<m or j<n:
            v1=v2=1000000
            if i<m:
                v1=nums1[i]
            if j<n:
                v2=nums2[j]
            if v1<v2:
                i+=1
                num.append(v1)
            else :
                j+=1
                num.append(v2)
            if len(num)==max_num:
                break
        return num[len(num)-1] if (m+n)%2!=0 else (num[len(num)-2]+num[len(num)-1])/2
    
cc=Solution().findMedianSortedArrays([1,3],[2])
print(cc)
                
                
           
            