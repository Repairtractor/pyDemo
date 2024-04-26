from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 逆序存储，也就是相加之后，还要逆序存储返回链表
# 制造一个假head表示新的节点头，然后使用next变量，同时遍历两个链表，然后使用 flag记录是否有进一位，有+1，直到遍历到两个链表尾部，时间复杂度O(n^2)
# 其实这道题相对简单，没有什么弯弯绕绕，只需要遍历两个链表，然后将和添加为一个新的链表就好，这里使用temp作为每次的数值和标志，每次/=10清理
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head=dummy_curr=ListNode()
        temp=0
        while l1 is not None or l2 is not None or temp!=0:
            if l1 is not None:
                temp+=l1.val
                l1=l1.next
            if l2 is not None:
                temp+=l2.val
                l2=l2.next
            dummy_curr.next=ListNode(temp%10)
            dummy_curr=dummy_curr.next
            temp//=10  # use integer division instead of float division

        return dummy_head.next

            
                
            