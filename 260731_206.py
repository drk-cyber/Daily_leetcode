#反转链表
from typing import Optional

#迭代法
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=None
        curr=head
        while curr:
            next_temp=curr.next
            curr.next=pre
            pre=curr
            curr=next_temp
        return pre

#递归法
'''from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归终止条件：空链表或只有一个节点
        if not head or not head.next:
            return head

        # 递归反转 head.next 及其之后的链表，返回新的头节点
        new_head = self.reverseList(head.next)

        # 此时，head.next 已经变成反转后链表的尾节点
        # 将 head 接到 tail 的后面
        head.next.next = head
        # 将 head 的 next 置空，防止形成环
        head.next = None
        # 返回新的头节点
        return new_head
'''