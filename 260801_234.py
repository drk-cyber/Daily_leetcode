#回文链表
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        pre = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = pre
            pre = curr
            curr = next_temp
        left,right=head,pre
        while right:
            if left.val!=right.val:
                return False
            right=right.next
            left=left.next
        return True